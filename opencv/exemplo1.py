import numpy as np
import cv2


tela = np.zeros((600,800,3), np.uint8)
cv2.circle(tela, (400,300), 20, (0,0,255), -1)
cv2.imshow("tela", tela)
cv2.waitKey(0)
