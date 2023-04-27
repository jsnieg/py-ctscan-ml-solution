#   Install required packages through pip in the script to run all.
import subprocess
import sys
import pkg_resources

#   Install the packages that are not present on someone else's / personal computer.

def install_dependecies():
    #   https://stackoverflow.com/questions/44210656/how-to-check-if-a-module-is-installed-in-python-and-if-not-install-it-within-t

    required_dependecies = {'torch', 'torchvision', 'torchaudio', 'numpy', 'pandas', 'kaggle'}
    installed_dependecies = { pkg.key for pkg in pkg_resources.working_set }

    missing = required_dependecies - installed_dependecies

    if missing:
        python = sys.executable
        subprocess.check_all([python, '-m', 'pip', 'install', *missing])

import numpy as np  #   numPy dependency for linear algebra.
import pandas as pd #   Data processing for CSV file I/O.

#   The input data files are only available with read-only permission in "../input/ dir."

#   Authentication for the Kaggle datasets.
import os
import kaggle

os.environ['KAGGLE_USERNAME'] = "?"
os.environ['KAGGLE_KEY'] = "?"

import torch
import torchvision
import torchvision.transforms as transforms

#   Main func- to run the script.

def main():
    install_dependecies()
