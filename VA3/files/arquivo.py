from PIL import Image, ImageOps
import cv2

diretorio_image = "../images-default/obediente.jpg"
diretorio_image_gerada = "../images-generated/obediente_diferente.jpg"

imagem = cv2.imread(diretorio_image)

altura, largura, canais = imagem.shape
nLargura = largura-1
nAltura = altura-1

# Abre a imagem
imagem = Image.open(diretorio_image)
imagem = imagem.convert("RGB")

try:
    nome_arquivo = "script.txt"
    arquivo = open(nome_arquivo, 'r+')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')

for x_largura in range(0, nLargura):
    for x_altura in range(0, nAltura):
        if imagem.getpixel((x_largura, x_altura)) == (0, 0, 0):
            imagem.putpixel( (x_largura, x_altura), (255, 255, 255))
            
        if imagem.getpixel((x_largura, x_altura)) == (255, 255, 255):
            arquivo.writelines(u'( x - '+ str(x_largura) + " , y - " + str(x_altura) + ')\n')

imagem_cinza = ImageOps.grayscale(imagem)
imagem_cinza.save(diretorio_image_gerada, quality=95)

image = cv2.imread(diretorio_image_gerada)

ponto = (largura / 2, altura / 2)
horizontal = cv2.getRotationMatrix2D(ponto, 180, 1.0)
rotacionar_horizontal = cv2.warpAffine(image, horizontal, (largura, altura))
cv2.imwrite(diretorio_image_gerada, rotacionar_horizontal)

image = cv2.imread(diretorio_image_gerada)

imagem_gausseano = cv2.GaussianBlur((image), (9,9), 7)
cv2.imwrite(diretorio_image_gerada, imagem_gausseano)

arquivo.close()