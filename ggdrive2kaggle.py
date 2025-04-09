# -*- coding: utf-8 -*-
"""
GGDrive2Kaggle - Upload a dataset from Google Drive to Kaggle automatically
"""

import os
import shutil
import argparse

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Install Kaggle API if not already installed
!pip install -q kaggle

# Setup argument parser
parser = argparse.ArgumentParser(description="Upload dataset from Google Drive to Kaggle")
parser.add_argument('--kaggle_json_path', type=str, required=True,
                    help='Path to kaggle.json file in Google Drive')
parser.add_argument('--dataset_folder', type=str, required=True,
                    help='Folder path where your dataset (.zip or files) are stored')
parser.add_argument('--kaggle_metadata_path', type=str, required=True,
                    help='Path to dataset-metadata.json file')
args = parser.parse_args()

# Set up Kaggle authentication
kaggle_dir = '/content/Kaggle'
if not os.path.exists(kaggle_dir):
    os.makedirs(kaggle_dir)

# Copy kaggle.json to working directory
shutil.copy2(args.kaggle_json_path, os.path.join(kaggle_dir, 'kaggle.json'))

# Set environment variable for Kaggle API
os.environ['KAGGLE_CONFIG_DIR'] = kaggle_dir

# Move dataset files (optional, depends on your project structure)
# Example: move all zipped datasets to target folder
dataset_target_dir = args.dataset_folder
os.makedirs(dataset_target_dir, exist_ok=True)

# (Optional) Example if you have raw files in /content to move
# !mv /content/*.zip {dataset_target_dir}

# Initialize Kaggle dataset metadata
!kaggle datasets init -p $kaggle_dir

# (Optional) If you want to manually write metadata.json:
# %%writefile /content/Kaggle/dataset-metadata.json
# {
#   "title": "Your Dataset Title",
#   "id": "yourusername/your-dataset-id",
#   "licenses": [
#     {
#       "name": "CC0-1.0"
#     }
#   ]
# }

# Copy the prepared metadata file to Kaggle directory
shutil.copy2(args.kaggle_metadata_path, os.path.join(kaggle_dir, 'dataset-metadata.json'))

# Create dataset on Kaggle
!kaggle datasets create -p $kaggle_dir --dir-mode zip
