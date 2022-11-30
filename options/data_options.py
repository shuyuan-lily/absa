import argparse
import os

class DataOptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.initialized = False

    def initialize(self):
        self.parser.add_argument('--apc_dataroot', required=True, help='path to apc data file, ending with .dat.apc')

    def parse(self):
        self.opt, unknown = self.parser.parse_known_args()
        return self.opt