import math
import os
import random
import shutil
from pathlib import Path

import cv2
import numpy as np
import torch
from PIL import Image, ExifTags
from torch.utils.data import Dataset
from tqdm import tqdm
from build_utils import datasets
from build_utils.utils import xyxy2xywh, xywh2xyxy
f=('D:/test.jpg')
# s = [datasets.exif_size(Image.open(f)) ]
# s=np.array(s, dtype=np.float64)
# print(s)
a=[np.zeros((0,5))]*5
print(a)