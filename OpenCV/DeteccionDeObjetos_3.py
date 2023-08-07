import cv2
import numpy as np

dibujar = False # Cambia de estado si se presiona el ratón
modo = True # En True dibuja rectángulos, en False; círculos. Para cambiar si usa la tecla m
ix, iy = -1, -1

# Función activa para el mouse
def dibuja(evento, x, y, flags, param):
    global ix, iy, dibujar, modo

    if evento == cv2.EVENT_LBUTTONDOWN:
        dibujar = True
        ix, iy = x, y

    elif evento == cv2.EVENT_MOUSEMOVE:
        if dibujar == True:
            if modo == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif evento == cv2.EVENT_LBUTTONUP:
        dibujar = False
        if modo == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

# Creación de una ventana en negro vacía
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',dibuja)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord('m'):
        modo = not modo
    elif k == 27:
        break
cv2.destroyAllWindows()

"""import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
"""