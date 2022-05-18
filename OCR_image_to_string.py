# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:52:48 2022

@author: sanjay a l
"""
import cv2
import pytesseract as pt
#import numpy as np
#enter the path of tessaract installed in the pc" 
pt.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                         #enter the path of the image to read"
img=cv2.imread("C:/Users/sanjay a l/Downloads/1.jpeg")
cap=cv2.resize(img,None,fx=0.5,fy=0.5)
gray=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

adaptive_threshold=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,85,11)
config ="--psm 3"
text=pt.image_to_string(adaptive_threshold,config=config)
#if the image is clear replace "adaptive_threshold" with "img"
print(text)

cv2.imshow("gray",gray)
cv2.imshow("adaptive th",adaptive_threshold)
cv2.waitKey(0)
