#   Install required packages through pip in the script to run all.
import subprocess
import sys
import pkg_resources

#   Install the packages that are not present on someone else's / personal computer.

def install_dependecies():
    #   https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t

    required_dependecies = {'torch', 'torchvision', 'torchaudio', 'numpy', 'pandas', 'kaggle', 'scikit-learn'}
    installed_dependecies = { pkg.key for pkg in pkg_resources.working_set }

    missing = required_dependecies - installed_dependecies

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing])

install_dependecies()

import numpy as np  #   numPy dependency for linear algebra.
import pandas as pd #   Data processing for CSV file I/O.

#   The input data files are only available with read-only permission in "../input/ dir."

#   Authentication for the Kaggle datasets.
import os
# import kaggle

import torch
import torchvision
import torchvision.transforms as transforms

#   Main function to run the script.

def main():
    #   If NVIDIA Cuda device is available on the machine use, if not use CPU as per default.
    cuda_device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"Running on - {cuda_device}")

    #   Download dataset from Kaggle using Kaggle's API doc.. & authenticate by requested private token. Change this if you want to use your own.
    os.environ['KAGGLE_USERNAME'] = "janiiuu"
    os.environ['KAGGLE_KEY'] = "512d72fa81bceaa26dfe9b8a685a158e"

    #   kaggle.api.authenticate()

    #   kaggle.api.dataset_download_files('', path='', unzip=True)

if __name__ == "__main__":
    main()