#====================================
# Funções para o projeto de visão computacional aplicada
#====================================

# Importando bibliotecas necessárias
import cv2
import matplotlib.pyplot as plt


#============================
# Definindo funções para o projeto
#============================

# Função para carregar uma imagem

def load_image(path: str):
    image = cv2.imread(path)

    if image is None:
        raise ValueError("Imagem não encontrada")
    return image