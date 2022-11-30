## Example Usage

Given that you have saved your new **apc** dataset under the `dataset/apc_datasets` folder, you can convert it directly to an **atepc** dataset, saved in the corresponding location `dataset/atepc_datasets`. 

With `absa` as your current directory, run the following command:
```
python convert_apc_to_atepc.py --apc_dataroot <relative_path_to_file>
```
This can be, for example: 
```
python convert_apc_to_atepc.py --apc_dataroot --apc_dataroot datasets/apc_datasets/001.larger_mbio/larger_mbio.train.dat.apc
```

The same thing can be done via bash scripting, with the `--apc_dataroot` argument of your choice (so modify this file as you wish):
```
bash utils/apc_to_atepc.sh
```