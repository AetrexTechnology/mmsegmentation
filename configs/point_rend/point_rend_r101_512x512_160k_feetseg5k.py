_base_ = [
    'C:/Users/zliu/Projects/mmsegmentation/configs/_base_/models/pointrend_r50.py',
    'C:/Users/zliu/Projects/mmsegmentation/configs/_base_/default_runtime.py',
    'C:/Users/zliu/Projects/configs/mmseg_configs/datasets/feetseg5k.py',
    'C:/Users/zliu/Projects/configs/mmseg_configs/schedules/schedule_160k.py'
]
norm_cfg = dict(type='BN', requires_grad=True)
model = dict(
    pretrained='C:/Users/zliu/Utilities/OpenMMLab/models/resnet101_v1c-e67eebb6.pth',
    backbone=dict(
        type='ResNetV1c',
        depth=101,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        dilations=(1, 1, 1, 1),
        strides=(1, 2, 2, 2),
        norm_cfg=norm_cfg,
        norm_eval=False,
        style='pytorch',
        contract_dilation=True),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        num_outs=4),
    decode_head=[
        dict(
            type='FPNHead',
            in_channels=[256, 256, 256, 256],
            in_index=[0, 1, 2, 3],
            feature_strides=[4, 8, 16, 32],
            channels=128,
            dropout_ratio=-1,
            num_classes=2,
            norm_cfg=norm_cfg,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
        dict(
            type='PointHead',
            in_channels=[256],
            in_index=[0],
            channels=256,
            num_fcs=3,
            coarse_pred_each_layer=True,
            dropout_ratio=-1,
            num_classes=2,
            align_corners=False,
            loss_decode=dict(
                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
    ],
    train_cfg=dict(
        num_points=128, 
        oversample_ratio=3, 
        importance_sample_ratio=0.75),
    test_cfg=dict(
        mode='whole',
        subdivision_steps=2,
        subdivision_num_points=512,
        scale_factor=2)
)
lr_config = dict(warmup='linear', warmup_iters=200)

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
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

