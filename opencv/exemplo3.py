import numpy as np
import cv2
import math


img_rgb = cv2.imread("moedas.jpg")

#img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#height, width = img.shape[:2]
#img = cv2.resize( img, ( int(width/2.0), int(height/2.0) ) )
#ret,bin = cv2.threshold(img,0,240,cv2.THRESH_BINARY_INV)

cv2.imshow("tela",img_rgb)
cv2.waitKey(0)
