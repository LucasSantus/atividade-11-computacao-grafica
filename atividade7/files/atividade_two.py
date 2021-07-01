import cv2

image = cv2.imread('../images-default/image_two.jpg')

azul, verde, vermelho = cv2.split(image)

image_two = cv2.merge((azul, verde, vermelho))
image_tree = cv2.merge((vermelho, verde, azul))
image_four = cv2.merge((verde, azul, vermelho))
image_five = cv2.merge((azul, vermelho, verde))

cv2.imshow("Azul", azul)
cv2.imshow("Verde", verde)
cv2.imshow("Vermelho", vermelho)

cv2.imshow("Nova Imagem ", image_two)
cv2.imshow("Nova Imagem - 2", image_tree)
cv2.imshow("Nova Imagem - 3", image_four)
cv2.imshow("Nova Imagem - 4", image_five)

cv2.imwrite("../images-generated/atividade_two/fruta_azul.jpg", azul)
cv2.imwrite("../images-generated/atividade_two/fruta_verde.jpg", verde)
cv2.imwrite("../images-generated/atividade_two/fruta_vermelho.jpg", vermelho)

print("\n-----------------------------------------------------")
print("\nImagens geradas!")
print("\nLocalização: /images-generated/atividade_two")
print("\n-----------------------------------------------------\n")

cv2.waitKey(0)
cv2.destroyAllWindows()