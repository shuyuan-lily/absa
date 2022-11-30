from pyabsa.utils.file_utils import convert_apc_set_to_atepc_set
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data")
    parser.add_argument('--apc_dataroot', required=True, help='path to apc data file, ending with .dat.apc')
    opt, unknown = parser.parse_known_args()
    print(opt)

    convert_apc_set_to_atepc_set(opt.apc_dataroot)
    # that is, the function will execute:
    ## convert_apc_set_to_atepc_set("datasets/apc_datasets/170.LargerCustom/larger_dataset_mbio_input.train.dat.apc")