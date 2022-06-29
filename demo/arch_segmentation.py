from argparse import ArgumentParser
import glob,os
from mmseg.apis import inference_segmentor, init_segmentor
from mmseg.core.evaluation import get_palette
import mmcv
import cv2
import numpy as np

'''
This python script runs in Windows system.
It may need a few modification for running in Linux system
'''

def extract_top_boundary(seg_img):
    seg_img = seg_img.astype(np.uint8)

    cnts,_ = cv2.findContours(seg_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cnts = sorted(cnts,key=lambda x:len(x),reverse=True)

    b = cnts[0].reshape(len(cnts[0]),-1)
    b = b[np.argsort(b[:,1],axis=0)]
    index = np.unique(b[:,0],return_index=True,axis=0)
    b = b[index[1]]

    top_boundary = np.zeros(seg_img.shape,dtype=np.int64)
    top_boundary[b[:,1],b[:,0]] = 1

    return top_boundary,b

def segmentor(img_name, model=None, args=None):
    # test a single image
    result = inference_segmentor(model, img_name)
    result,boundary = extract_top_boundary(result[0])
    out_img_name = os.path.join(args.show_dir, img_name.split('\\')[-1])  # path seperator for Windows
    model.show_result(
        img_name, [result], palette=get_palette(args.palette), show=False, opacity=args.opacity, out_file=out_img_name)

    return boundary

def main():
    parser = ArgumentParser()
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument('--img-path', help='The path for images to be segmented')
    parser.add_argument('--show-dir', help='The path for output images')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--palette',
        default='cityscapes',
        help='Color palette used for segmentation map')
    parser.add_argument(
        '--opacity',
        type=float,
        default=0.5,
        help='Opacity of painted segmentation map. In (0, 1] range.')
    args = parser.parse_args()

    # delete all images in args.show_dir
    files = glob.glob(os.path.join(args.show_dir, '*.png'))
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    # build the model from a config file and a checkpoint file
    model = init_segmentor(args.config, args.checkpoint, device=args.device)

    imgs_name_list = glob.glob(args.img_path + '/*.png')
    if hasattr(model, 'module'):
        model = model.module

    kwargs = {'model': model, 'args': args}
    results = mmcv.track_progress(segmentor, imgs_name_list, **kwargs)

    # all top boundary of arch are contained in this pkl file
    output_file = os.path.join(args.show_dir, 'output.pkl')
    mmcv.dump(results,output_file)

if __name__ == '__main__':
    main()
