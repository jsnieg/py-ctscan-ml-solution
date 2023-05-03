""" Install required packages through pip in the script to run all. """
import subprocess
import sys
import pkg_resources

""" Install the packages that are not present on someone else's / personal computer. """
def install_dependecies():
    #   https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t

    required_dependecies = {'torch', 'torchvision', 'torchaudio', 'numpy', 'pandas', 'kaggle', 'scikit-learn'}
    installed_dependecies = { pkg.key for pkg in pkg_resources.working_set }

    missing = required_dependecies - installed_dependecies

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing])

install_dependecies()   #   Runs the function...

import numpy as np  #   numPy dependency for linear algebra.
import pandas as pd #   Data processing for CSV files I/O.

""" The input data files are only available with read-only permission in "../input/ dir. """

""" Authentication for the Kaggle datasets using Kaggle's API. """
import os
# import kaggle

import torch
import torchvision
import torchvision.transforms as transforms

from sklearn.preprocessing import LabelEncoder

""" Neural networks will be constructed using the torch.nn dependency. """

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from torch.utils.data.sampler import SubsetRandomSampler
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

""" Main function running the machine model. """

def main():
    """ Checking for available CUDA devices else run on CPU by default. """
    cuda_device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"Running On - {cuda_device}")

""" Main. """

if __name__ == "__main__":
    main()