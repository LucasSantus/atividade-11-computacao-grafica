import numpy as np
import cv2

def gerar_imagem(nome, email):
    largura = 500
    altura = 500

    # Cria uma nova imagem(500x500 e 3 canais RGB)
    imagem = np.zeros((altura, largura, 3), dtype=np.uint8)
    x=0
    y=0

    # Percorrendo a imagem
    for x in range(0, altura):
        for y in range(0, largura):
            if x <= altura/2:
                imagem[x,y] = [0,0,0]
            else:
                imagem[x,y] = [0,255,0]

    # Desenha o texto com a variavel em preto, no centro
    fonte = cv2.FONT_HERSHEY_PLAIN
    escala = 1.3
    grossura = 1

    # Pega o tamanho (altura e largura) do texto em pixels
    tamanho, _ = cv2.getTextSize(nome, fonte, escala, grossura)
    
    # Escreve o texto de acordo com o tamanho da imagem
    cv2.putText(imagem, nome, (int(largura / 2 - tamanho[0] / 2), int(altura / 2 / 2)), fonte, escala, (255, 255, 255), grossura)
    cv2.putText(imagem, email, (int(largura / 2 - tamanho[0] / 2), int(altura - (altura / 2 / 2 ))), fonte, escala, (0, 0, 0), grossura)
    cv2.imwrite("imagem.jpg", imagem)

    # Ponto no centro da figura
    ponto = (largura / 2, altura / 2) 

    # Rotaciona imagem verticalmente
    rotacao_vertical = cv2.getRotationMatrix2D(ponto, 90, 1.0)
    rotacionar_vertical = cv2.warpAffine(imagem, rotacao_vertical, (largura, altura))
    cv2.imwrite("imagem_vertical.jpg", rotacionar_vertical)

    # Rotaciona imagem horizontalmente
    rotacao_horizontal = cv2.getRotationMatrix2D(ponto, 180, 1.0)
    rotacionar_horizontal = cv2.warpAffine(imagem, rotacao_horizontal, (largura, altura))
    cv2.imwrite("imagem_horizontal.jpg", rotacionar_horizontal)

if __name__ == '__main__':
    nome = 'Lucas Eduardo de Oliveira Santos'
    email = 'lucas.oliveira@aluno.unincor.edu.br'
    gerar_imagem(nome, email)