import numpy as np
import cv2

# Tamanho padrão da imagem
largura = 500
altura = 500

def generated_image():
    # Cria uma nova imagem(500x500 e 3 canais RGB)
    image = np.zeros((altura, largura, 3), dtype=np.uint8)
    return image

def mostraVariavel(imagem, nome):
    for y in range(0, altura):
        for x in range(0, largura):
            # if x > 250:
            #     cv2.rectangle(imagem, (0, 0), (x, y), (0, 255, 255), -1)
            # elif x < 250:
                cv2.rectangle(imagem, (0, 0), (x, y), (0,128,0), -1)

    # Preenche o fundo de amarelo
    # cv2.rectangle(imagem, (0, 0), (largura, altura), (0, 255, 255), -1)
    # Desenha o texto com a variavel em preto, no centro
    fonte = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    escala = 1
    grossura = 2

    # Pega o tamanho (altura e largura) do texto em pixels
    tamanho, _ = cv2.getTextSize(nome, fonte, escala, grossura)

    # Desenha o texto no centro
    cv2.putText(imagem, nome, (int(largura / 2 - tamanho[0] / 2), int(altura / 2 + tamanho[1] / 2)), fonte, escala, (255, 255, 255), grossura)
    # cv2.putText(imagem, texto, (int(largura / 2 - tamanho[0] / 2), 450), fonte, escala, (0, 0, 0), grossura)
    cv2.imwrite("teste.jpg", imagem)

if __name__ == '__main__':
    image = generated_image()
    mostraVariavel(image, 'Lucas Eduardo de Oliveira Santos')

# import cv2
# import numpy as np
# img=np.zeros((320,600),dtype=np.uint8)
# cv2.putText(img,"FONT_HERSHEY_SIMPLEX",(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,255)
# cv2.putText(img,"FONT_HERSHEY_COMPLEX",(10,60),cv2.FONT_HERSHEY_COMPLEX,1,255)
# cv2.putText(img,"FONT_HERSHEY_DUPLEX",(10,90),cv2.FONT_HERSHEY_DUPLEX,1,255)
# cv2.putText(img,"FONT_HERSHEY_TRIPLEX",(10,120),cv2.FONT_HERSHEY_TRIPLEX,1,255)
# cv2.putText(img,"FONT_HERSHEY_COMPLEX_SMALL",(10,150),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,255)
# cv2.putText(img,"FONT_HERSHEY_PLAIN",(10,180),cv2.FONT_HERSHEY_PLAIN,1,255)
# cv2.putText(img,"FONT_HERSHEY_SCRIPT_COMPLEX",(10,210),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,255)
# cv2.putText(img,"FONT_ITALIC",(10,240),cv2.FONT_ITALIC,1,255)
# cv2.putText(img,"QT_FONT_BLACK",(10,270),cv2.QT_FONT_BLACK,1,255)
# cv2.putText(img,"QT_FONT_NORMAL",(10,300),cv2.QT_FONT_NORMAL,1,255)
# cv2.imshow("janela",img)
# cv2.imwrite("fonte_opencv.jpg",img)
# cv2.waitKey(0)