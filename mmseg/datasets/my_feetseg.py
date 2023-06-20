# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MyFeetSegDataset(CustomDataset):
    """feet segmentation dataset. 0 stands for background, 1 for left foot, 2 for right foot
    which is included in 3 categories.
    """

    CLASSES = ('background','left foot', 'right foot')

    PALETTE = [[120,120,120],[128, 64, 128], [192, 96, 128]]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='.png',
                 **kwargs):
        super(MyFeetSegDataset, self).__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            **kwargs)
