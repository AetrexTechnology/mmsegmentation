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
|   |   |   |   ├── xxx{img_suffix}
|   |   |   |   ├── yyy{img_suffix}
│   │   ├── val_set
│   │   │   ├── images
|   |   |   |   ├── zzz{img_suffix}
|   |   |   |   ├── www{img_suffix}
│   │   │   ├── annotations
|   |   |   |   ├── zzz{img_suffix}
|   |   |   |   ├── www{img_suffix}
│   |   ├── train_list.txt
│   │   ├── val_list.txt

```
