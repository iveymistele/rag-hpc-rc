Using the PyTorch container:

```bash
module load apptainer pytorch/2.4.0

apptainer exec $CONTAINERDIR/pytorch-2.4.0.sif pip install transformers datasets

```

These packages are provided by Hugging Face (more details on Hugging Face in a bit).

For the fine-tuning example we will do later today, we will also need to install the accelerate and evaluate packages.

```bash
apptainer exec $CONTAINERDIR/pytorch-2.4.0.sif pip install accelerate evaluate
```

