# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MyFeetArchDataset(CustomDataset):
    """feet arch dataset. 0 stands for background,
    which is included in 2 categories.
    """

    CLASSES = ('background','arch')

    PALETTE = [[120,120,120],[128, 64, 128]]

    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix='_ann.png',
                 **kwargs):
        super(MyFeetArchDataset, self).__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            **kwargs)        
