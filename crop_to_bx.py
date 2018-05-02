#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 18:23:45 2018

@author: shanthakumarp
"""

import cv2

colored_img = cv2.imread('macine_id_crop.png')
img_copy = colored_img.copy()
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

#gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
_,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
_, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours

# for each contour found, draw a rectangle around it on original image
for contour in contours:
    # get rectangle bounding contour
    [x,y,w,h] = cv2.boundingRect(contour)

    # discard areas that are too large
    if h>300 and w>300:
        continue

    # discard areas that are too small
    if h<30 or w<30:
        continue

    # draw rectangle around contour on original image
    cv2.rectangle(img_copy,(x,y),(x+w,y+h),(0,255,0),2)

# write original image with added contours to disk  
cv2.imwrite("contoured6.jpg", img_copy) 