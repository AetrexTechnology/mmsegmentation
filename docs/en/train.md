## Train a model

MMSegmentation implements distributed training and non-distributed training,
which uses `MMDistributedDataParallel` and `MMDataParallel` respectively.

All outputs (log files and checkpoints) will be saved to the working directory,
which is specified by `work_dir` in the config file.

By default we evaluate the model on the validation set after some iterations, you can change the evaluation interval by adding the interval argument in the training config.

```python
evaluation = dict(interval=4000)  # This evaluate the model per 4000 iterations.
```

**\*Important\***: The default learning rate in config files is for 4 GPUs and 2 img/gpu (batch size = 4x2 = 8).
Equivalently, you may also use 8 GPUs and 1 imgs/gpu since all models using cross-GPU SyncBN.

To trade speed with GPU memory, you may pass in `--cfg-options model.backbone.with_cp=True` to enable checkpoint in backbone.

### Train on a single machine

#### Train with a single GPU

official support:

```shell
sh tools/dist_train.sh ${CONFIG_FILE} 1 [optional arguments]
```

experimental support (Convert SyncBN to BN):

```shell
python tools/train.py ${CONFIG_FILE} [optional arguments]
```

If you want to specify the working directory in the command, you can add an argument `--work-dir ${YOUR_WORK_DIR}`.

#### Train with multiple GPUs

```shell
sh tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM} [optional arguments]
```

Optional arguments are:

- `--no-validate` (**not suggested**): By default, the codebase will perform evaluation at every k iterations during the training. To disable this behavior, use `--no-validate`.
- `--work-dir ${WORK_DIR}`: Override the working directory specified in the config file.
- `--resume-from ${CHECKPOINT_FILE}`: Resume from a previous checkpoint file (to continue the training process).
- `--load-from ${CHECKPOINT_FILE}`: Load weights from a checkpoint file (to start finetuning for another task).
- `--deterministic`: Switch on "deterministic" mode which slows down training but the results are reproducible.

Difference between `resume-from` and `load-from`:

- `resume-from` loads both the model weights and optimizer state including the iteration number.
- `load-from` loads only the model weights, starts the training from iteration 0.

An example:

```shell
# checkpoints and logs saved in WORK_DIR=work_dirs/pspnet_r50-d8_512x512_80k_ade20k/
# If work_dir is not set, it will be generated automatically.
sh tools/dist_train.sh configs/pspnet/pspnet_r50-d8_512x512_80k_ade20k.py 8 --work_dir work_dirs/pspnet_r50-d8_512x512_80k_ade20k/ --deterministic
```

**Note**: During training, checkpoints and logs are saved in the same folder structure as the config file under `work_dirs/`. Custom work directory is not recommended since evaluation scripts infer work directories from the config file name. If you want to save your weights somewhere else, please use symlink, for example:

```shell
ln -s ${YOUR_WORK_DIRS} ${MMSEG}/work_dirs
```

### Train for segmentation of feet arch

After preparing all configs, we use `dist_train.sh` to launch training jobs. We can set some environment variables in commands.

```shell
CONFIG_FILE = 'your path'/mmsegmentation/configs/point_rend/point_rend_r101_512x512_160k_feetarch5k.py
GPU_NUM = 2
WORK_DIR = 'optional. you can specify the output directory'
CHECKPOINT_FILE = 'optional. you can specify a pretrained model or a checkpoint file'

CUDA_VISIBLE_DEVICES=0,1,2,3 sh tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM} --work-dir ${WORK_DIR} --load-from ${CHECKPOINT_FILE}
```
