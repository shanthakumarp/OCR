#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:57:13 2018

@author: shanthakumarp
"""

import cv2
img = cv2.imread('add1.jpg', 0)
ret, thresh = cv2.threshold(img , 10, 255, cv2.THRESH_OTSU)

print "Threshold selected: ", ret
cv2.imwrite("debug.png", thresh)

