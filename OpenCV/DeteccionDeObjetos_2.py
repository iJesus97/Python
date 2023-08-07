import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
	pass

cv2.namedWindow('image')
cv2.createTrackbar('Hue Minimo','image',0,255, nothing)
cv2.createTrackbar('Hue Maximo','image',0,255, nothing)
cv2.createTrackbar('Saturation Minimo','image',0,255, nothing)
cv2.createTrackbar('Saturation Maximo','image',0,255, nothing)
cv2.createTrackbar('Value Minimo','image',0,255, nothing)
cv2.createTrackbar('Value Maximo','image',0,255, nothing)

while(1):
   hMin = cv2.getTrackbarPos('Hue Minimo','image')
   hMax = cv2.getTrackbarPos('Hue Maximo','image')
   sMin = cv2.getTrackbarPos('Saturation Minimo','image')
   sMax = cv2.getTrackbarPos('Saturation Maximo','image')
   vMin = cv2.getTrackbarPos('Value Minimo','image')
   vMax = cv2.getTrackbarPos('Value Maximo','image')
   
   _, frame = cap.read()
   
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

   # define range of blue color in HSV
   lower=np.array([hMin,sMin,vMin])
   upper=np.array([hMax,sMax,vMax])
   lower_blue = np.array([hMin,sMin,vMin])
   upper_blue = np.array([hMax,sMax,vMax])

   # Threshold the HSV image to get only blue colors
   mask = cv2.inRange(hsv, lower_blue, upper_blue)

   # Bitwise-AND mask and original image
   res = cv2.bitwise_and(frame,frame, mask= mask)

   cv2.imshow('frame',frame)
   cv2.imshow('mask',mask)
   cv2.imshow('res',res)
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()