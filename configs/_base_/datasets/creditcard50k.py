# dataset settings
dataset_type = 'MyCreditCardDataset'
data_root = 'C:/Users/zliu/Projects/FeetReferenceModel_Mask_RCNN/aetrex_module/data/dataset'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
crop_size = (512, 512)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', reduce_zero_label=False),
    dict(type='Resize', img_scale=(1024, 512), ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1024, 512),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        flip=True,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir=[
                 'russian_latest/training_card_Nov11/train/images',
                 'russian_latest/additional_training_augment_credit_card_Dec17_430/train/images',
                 'russian_latest/additional_training_credit_card_Dec17_430/train/images',
                 'credit_card_data1/train/images',
                 #'russian_latest/training_augment_card_Nov11/train/images',
                 ],
        ann_dir=[
                 'russian_latest/training_card_Nov11/train/annotations',
                 'russian_latest/additional_training_augment_credit_card_Dec17_430/train/annotations',
                 'russian_latest/additional_training_credit_card_Dec17_430/train/annotations',
                 'credit_card_data1/train/annotations',
                 #'russian_latest/training_augment_card_Nov11/train/annotations',
                 ],
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir=[
                 'russian_latest/training_card_Nov11/val/images',
                 'russian_latest/additional_training_augment_credit_card_Dec17_430/val/images',
                 'russian_latest/additional_training_credit_card_Dec17_430/val/images',
                 'credit_card_data1/val/images',
                 #'russian_latest/training_augment_card_Nov11/val/images',
                 ],
        ann_dir=[
                 'russian_latest/training_card_Nov11/val/annotations',
                 'russian_latest/additional_training_augment_credit_card_Dec17_430/val/annotations',
                 'russian_latest/additional_training_credit_card_Dec17_430/val/annotations',
                 'credit_card_data1/val/annotations',
                 #'russian_latest/training_augment_card_Nov11/val/annotations',
                 ],
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='my_test_images/images',
        ann_dir='my_test_images/annotations',
        pipeline=test_pipeline))