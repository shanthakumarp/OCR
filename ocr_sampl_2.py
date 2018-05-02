#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:39:22 2018

@author: shanthakumarp
"""

import pylab as pl
import matplotlib.pyplot as plt

import numpy as np
from scipy import ndimage
import cv2
from PIL import Image


colored_img = cv2.imread('aad2_crop.png')
img_copy = colored_img.copy()
gray1 = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
plt.imshow(gray1)


img = pl.imread("aad2_crop.png")[:, :, 0].astype(np.uint8)
plt.imshow(img)
img2 = ndimage.binary_erosion(img, iterations=40)
img3 = ndimage.binary_dilation(img2, iterations=40)
labels, n = ndimage.label(img3)
counts = np.bincount(labels.ravel())
counts[0] = 0
img4 = labels==np.argmax(counts)
img5 = ndimage.binary_fill_holes(img4)
result = ~img & img5
result = ndimage.binary_erosion(result, iterations=3)
result = ndimage.binary_dilation(result, iterations=3)
#pl.imshow(result, cmap="gray")
