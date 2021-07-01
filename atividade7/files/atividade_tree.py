import numpy as np
import cv2
imagem = cv2.imread("../images-default/image_tree.bmp", 0)
tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagem, 127, 255, tipo)

modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;
contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

objeto = contornos[0]
area = cv2.contourArea(objeto)

print(area)

cv2.waitKey(0)
cv2.destroyAllWindows()