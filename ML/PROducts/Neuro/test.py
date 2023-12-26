from skimage import io
from skimage import color
from skimage.util import img_as_float
from skimage.segmentation import slic
from matplotlib import pyplot as plt
import os
image = img_as_float(io.imread(f'./datasets/landscapes/10}'))