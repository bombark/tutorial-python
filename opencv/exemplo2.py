import numpy as np
import cv2
import math

#img_rgb = cv2.imread("moedas.jpg")

#img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#height, width = img.shape[:2]
#img = cv2.resize( img, ( int(width/2.0), int(height/2.0) ) )
#ret,bin = cv2.threshold(img,0,240,cv2.THRESH_BINARY_INV)
#print(ret)


tela = np.zeros((600,800,3), np.uint8)
for i in range(400):
	dy = int( math.sin( i*3.141592/180.0 ) * 80 )
	cv2.circle(tela, (100+i,300+dy), 20, (0,0,255), -1)
	cv2.imshow('image',tela)
	key = cv2.waitKey(20)
	print(dy)
