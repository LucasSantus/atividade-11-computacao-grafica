import cv2

image = cv2.imread("../images-default/image_one.jpg")
altura, largura, canais = image.shape
nLargura = largura-1
nAltura = altura-1
x=0
y=0

for x in range(0, nLargura):
    for y in range(0, nAltura):
        if image[x,y][0] == 255 and image[x,y][1] == 255 and image[x,y][2] == 255:
            image[x,y] = [0,0,0]

cv2.imwrite("../images-generated/atividade_one/atividade_one.jpg", image)

print("\n-----------------------------------------------------")
print("\nImagem gerada!")
print("\nLocalização: /images-generated/atividade_one")
print("\n-----------------------------------------------------\n")