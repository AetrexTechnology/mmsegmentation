# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MyCreditCardDataset(CustomDataset):
    """credit card dataset. 0 stands for background,
    which is included in 2 categories.
    """

    CLASSES = ('background','credit card')

    PALETTE = [[120,120,120],[128, 64, 128]]

    def __init__(self,
                 img_suffix='.jpg',
                 seg_map_suffix='_mask2.png',
                 **kwargs):
        super(MyCreditCardDataset, self).__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            **kwargs)
        assert self.file_client.exists(self.img_dir)
