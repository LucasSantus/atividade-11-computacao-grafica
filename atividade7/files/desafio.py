from PIL import Image
import cv2

diretorio = "../images-default/image_four.png"

# Descobrindo o tamanho da imagem
image = cv2.imread(diretorio)
altura, largura, canais = image.shape
nLargura = largura-1
nAltura = altura-1

# Abre a imagem
imagem = Image.open(diretorio)

try:
    nome_arquivo = "coordenadas.txt"
    arquivo = open(nome_arquivo, 'r+')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'w+')

for x in range(0, nLargura):
    for y in range(0, nAltura):
        if imagem.getpixel((x,y)) == (237, 28, 36):
            arquivo.writelines(u'('+ str(x) + " , " + str(y) + ')\n')

arquivo.close()