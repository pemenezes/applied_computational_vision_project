# Projeto desenvolvido por:
# Pedro Henrique menezes Mariano Silva / RM97432


# O projeto tem como objetivo criar um script capaz de ler uma imagem, processa-la, 
# segmentar objetos, detectar e delimitar regiões e contar objetos

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


# Função para converter a imagem para escala de cinza
def convert_2_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Função para mostrar a imagem usando Matplotlib
def show_image (image , title = "Imagem"):
    plt.imshow(image, cmap='gray') # Exibe a imagem usando Matplotlib. cmap='gray' para escala de cinza.
    plt.title(title)
    plt.axis('off')
    plt.show()


# Função para plotar o histograma da imagem
def plot_histogram(image, title = "Histograma"):
    plt.hist(image.ravel(), bins=256, range=[0, 256]) # Plota o histograma da imagem. ravel() achata a imagem em um array 1D.
    plt.title("Histograma de intensidade")
    plt.xlabel("Intensidade de pixel")
    plt.ylabel("Quantidade de pixels")
    plt.show()


# Função para ajuste de brilho e contraste
def adjust_brightness_contrast(image, alpha = 1.0, beta = 0):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


# Função para equalizar a imagem
def equalize_image (image):
    return cv2.equalizeHist(image)


# Função para calcular métricas simples da imagem
def calculate_metrics(image):
    brightness = image.mean()
    contrast = image.std()
    return brightness, contrast