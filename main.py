# Arquivo onde iremos executar o projeto, utilizando as funções criadas no arquivo funcoes.py

# importando todas as funções do arquivo funcoes.py

from funcoes import *


# Carrega a imagem
if __name__ == "__main__":
    img = load_image("pexels-caleb-falkenhagen-216813613-30803006.jpg")
    print("Shape imagem colorida:", img.shape)


# Converte para a escala de cinza
    gray = convert_2_gray(img)
    print("Shape imagem grayscale:", gray.shape)


# Mostra a imagem em escala de cinza e plota o histograma
    show_image(gray, "Imagem Original (Gray)")
    plot_histogram(gray)


# Calcula métricas de brilho e contraste originais

    brightness, contrast = calculate_metrics(gray)
    print("--- MÉTRICAS ORIGINAIS ---")
    print("Brilho médio: ", brightness)
    print("Contraste (desvio padrão): ", contrast)



# Ajusta o brilho e contraste da imagem
    adjusted = adjust_brightness_contrast(gray, alpha=1.3, beta=30)
    show_image(adjusted, "Brilho e Contraste Ajustados")
    plot_histogram(adjusted)


# Calcula métricas após ajuste
    brightness_adj, contrast_adj = calculate_metrics(adjusted)
    print("\n--- MÉTRICAS APÓS AJUSTE ---")
    print("Brilho médio: ", brightness_adj)
    print("Contraste (desvio padrão): ", contrast_adj)

# Equaliza a imagem e mostra o resultado
    equalized = equalize_image(adjusted)
    show_image(equalized, "Imagem Equalizada")
    plot_histogram(equalized)

# Calcula métricas após equalização
    brightness_eq, contrast_eq = calculate_metrics(equalized)
    print("\n--- MÉTRICAS APÓS EQUALIZAÇÃO ---")
    print("Brilho médio: ", brightness_eq)
    print("Contraste (desvio padrão): ", contrast_eq)