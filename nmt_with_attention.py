from __future__ import absolute_import, division, print_function

# 要是只想仅使用CPU
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import tensorflow as tf

tf.enable_eager_execution()

import matplotlib.pyplot as plt

import sklearn.model_selection import train_test_split

import unicodedata
import re
import numpy as np
import time

print(tf.__vsersion__)
