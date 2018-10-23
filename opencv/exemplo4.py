import numpy as np
import cv2
import math


video = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
