# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MyFeetSegDataset(CustomDataset):
    """feet segmentation dataset. 0 stands for background, 1 for foot
    which is included in 2 categories.
    """

    CLASSES = ('background','feet')

    PALETTE = [[120,120,120],[255, 64, 128]]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs):
        super(MyFeetSegDataset, self).__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            **kwargs)
