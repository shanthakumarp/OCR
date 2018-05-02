#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 18:59:08 2018

@author: shanthakumarp
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt


large = cv2.imread('macine_id_crop.png')
rgb = cv2.pyrDown(large)
small = cv2.cvtColor(large, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
connected_copy = connected.copy()

# using RETR_EXTERNAL instead of RETR_CCOMP
_, contours, hierarchy = cv2.findContours(connected_copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

mask = np.zeros(bw.shape, dtype=np.uint8)
#print mask

for idx in range(0, len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
#    print mask
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
#    print r

    if r > 0.45 and w > 8 and h > 8:
        cv2.rectangle(large, (x-4, y-4), (x+w+2, y+h+2), (255,0,0), 2)

#plt.imshow('rects', rgb)
cv2.imwrite("contoured8.jpg", large) 

from PIL import Image
Image.fromarray(large).show()
