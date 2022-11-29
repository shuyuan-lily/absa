# Checkpoints

This folder contains a range of trained model weights. You can either use them to draw inferences on texts directly, or treat them as starting points for fine-tuning new models.

These checkpoint folders are named after:

```
<model_name>_<dataset_name>
```

Followed by three metrics:

* `apcacc` Aspect Polarity Classification (APC) Accuracy, 
* `apcf1` F1 Accuracy for Aspect Polarity Classification (APC), and 
* `atef1` F1 Accuracy for Aspect Term Extraction (ATE)