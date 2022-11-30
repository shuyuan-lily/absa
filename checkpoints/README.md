# Checkpoints

This folder contains a range of trained model weights. You can either use them to draw inferences on texts directly, or treat them as starting points for fine-tuning new models.

These checkpoint folders are named after:

```
<model_name>_<dataset_name>_<apcacc>_<apcf1>_<atef1>
```

The name is followed by three metrics:

* `apcacc`  Aspect Polarity Classification (APC) Accuracy, 
* `apcf1`  F1 Score for Aspect Polarity Classification (APC), and 
* `atef1`  F1 Score for Aspect Term Extraction (ATE)

## Usage

To load the weights from a checkpoint, simply put the pathname as the variable and feed it as a keyword argument after `checkpoint` when you define an `aspect_extractor`. Here is an example:

```
```

## To Do

Find some ways to upload the checkpoints online, so that you don't need to push & pull the weight files onto GitHub, which is slow and tedious.
