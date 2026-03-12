# Arquivo onde iremos executar o projeto, utilizando as funções criadas no arquivo funcoes.py

#importando as funções do arquivo funcoes.py

from funcoes import *

if __name__ == "__main__":
    img = load_image("pexels-caleb-falkenhagen-216813613-30803006.jpg")

    print("Shape imagem colorida:", img.shape)

    show_image(img, "Imagem Original (Colorida)")