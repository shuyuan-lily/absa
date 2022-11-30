# Aspect-Based Sentiment Analysis for mBio Media Quotations Dataset 

Hi! This is the folder that contains the relevant tools to run article analysis with Aspect-Based Sentiment Analysis (ABSA). 

Here's a brief overview of the folder:
```tree
absa
├── experiment_demos  ## contains .ipynb notebooks for past experiments
│   └── ... 
├── datasets  ## past dataset parsed to trainable format
│   └── ...
├── utils
│   └── ...
├── train.py
└── test.py
```

The models are largely based on the work by [Yang Heng](https://github.com/yangheng95)'s [work on PyABSA](https://github.com/yangheng95/PyABSA). If any of the code in our absa toolkit goes problematic, you might find his guidelines helpful!

## What is Aspect-Based Sentiment Analysis?

In plain-old sentiment analysis (classification), we put a sentence as input and obtain a prediction of whether the sentence belongs to the `positive`, `negative`, or `neutral` class. 

In Aspect-Based Sentiment Analysis, there is one more task on top. The task involves identifying the **aspect term**, and outputting a corresponding sentiment that the speaker holds **towards** that aspect.

In the implementation provided by this repository, the task is carried out in a pipeline manner. We first identify the aspect terms (token classification)and then perform sentiment classification. (The nomenclature below are adapted from the original repository.)

#### 1. Aspect Term Extraction (ATE)



#### 2. Aspect Polarity Classification (APC)



## Usage

### Getting Started

### Example Usage

## Possible Next Steps

### Improving the integration of this toolkit to our dataset

### Use BERT tags to identify crops before feeding into model
Described in [this](https://github.com/orgs/chicago-cdac/projects/7/views/1) issue.

The idea is that, given that we have a 


## Additional Information
Here is the complete structure of this folder. 
```tree
absa
├── experiment_demos
├── datasets
│   ├── apc_datasets
│   │   └── 160.CustomDataset
│   │       ├── mbio_custom.test.dat.apc
│   │       └── mbio_custom.train.dat.apc
│   └── atepc_datasets
│       └── 160.CustomDataset
├── utils
│   └── csv_to_atepc.py
├── train.py
└── test.py
```
