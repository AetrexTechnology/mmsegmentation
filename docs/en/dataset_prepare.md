## Prepare datasets

Data folder structure is as follows.

```none
mmsegmentation
├── mmseg
├── tools
├── configs
├── data
│   ├── arch_scans_324
│   │   ├── train_set
│   │   │   ├── images
|   |   |   |   ├── xxx{img_suffix}
|   |   |   |   ├── yyy{img_suffix}
│   │   │   ├── annotations
|   |   |   |   ├── xxx{seg_map_suffix}
|   |   |   |   ├── yyy{seg_map_suffix}
│   │   ├── val_set
│   │   │   ├── images
│   │   │   ├── annotations
│   |   |

```

The example of an annotated RGB image (xxx.png) and its segmentation annotation (xxx_ann.png) is given as follows:

![RGB](../../resources/feet_imgs/Tia_scan3_left_front_segmentation.png)
![ANN](../../resources/feet_imgs/Tia_scan3_left_front_ann.png)

The annotation image contains two classes, 0 for background and 1 for foreground, which have been converted to pseudo color from gray for visualization.
