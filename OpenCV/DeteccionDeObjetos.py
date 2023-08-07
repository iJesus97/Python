import cv2
import numpy as np

cam = cv2.VideoCapture(0)
kernel = np.ones((5,5), np.uint8)

while True:
	ret, frame = cam.read()
	rangomax = np.array([5, 216, 255])
	rangomin = np.array([0, 50, 105])
	mascara = cv2.inRange(frame, rangomin, rangomax)
	opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
	cv2.putText(frame, "Indicador de salida", (133, 170), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 0))
	cv2.putText(frame, "Indicador de elemento de seguridad", (220, 280), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0))
	cv2.rectangle(frame, (150, 190), (150 + 120, 150 + 100), (255, 255, 0), 3)
	cv2.rectangle(frame, (320, 190), (300 + 95, 150 + 100), (0, 255, 0), 3)
	cv2.imshow('Camara', frame)
	k = cv2.waitKey(1) & 0xFF

	if k == 27:
		break