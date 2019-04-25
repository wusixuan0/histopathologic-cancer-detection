import numpy as np
import pandas as pd
import os
from glob import glob
from PIL import Image

train_labels = pd.read_csv("./dataset/train_labels.csv")
train_labels.head()

id_label_map = {k:v for k,v in zip(train_labels.id.values, train_labels.label.values)}
{k: id_label_map[k] for k in list(id_label_map)[:10]}

def get_id_from_file_path(file_path):
    return file_path.split(os.path.sep)[-1].replace('.tif', '')
