## Prepare datasets

Data folder structure is as follows.

```none
mmsegmentation
├── mmseg
├── tools
├── configs
├── data
│   ├── feet_arch
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
│   |   ├── train_list.txt
│   │   ├── val_list.txt

```
