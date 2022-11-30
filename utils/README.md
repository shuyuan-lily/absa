## Dataset-Related Utility Functions

Before proceeding, make sure you have a general idea of the datasets and formats by going through this `README.md` writeup under the `datasets` directory. 

### Obtaining apc train/test data files from .csv files 

TODO: write this part.

### Converting apc train/test data files to atepc train/test data files

Given that you have saved your new **apc** dataset under the `dataset/apc_datasets` folder, you can convert it directly to an **atepc** dataset, saved in the corresponding location `dataset/atepc_datasets`. 

**With `absa` as your current directory**, run the following command:
```
python convert_apc_to_atepc.py --apc_dataroot <relative_path_to_file>
```
This can be, for example: 
```
python convert_apc_to_atepc.py --apc_dataroot --apc_dataroot datasets/apc_datasets/001.larger_mbio/larger_mbio.train.dat.apc
```

The same thing can be done via bash scripting, with the `--apc_dataroot` argument of your choice (so modify this file as you wish):
```
bash utils/example_scripts/apc_to_atepc.sh
```

### Stratified train-test split

TODO: implement this and write more.