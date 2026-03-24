# 🔍 Visão Computacional Aplicada — Processamento e Análise de Imagens

> Projeto acadêmico de visão computacional com foco em pré-processamento, análise e segmentação de imagens utilizando OpenCV e Python.

---

## 👤 Autor

**Pedro Henrique Menezes Mariano Silva**  
RM: 97432

---

## 🎯 Objetivo

Desenvolver um script capaz de:

- Carregar e exibir imagens
- Converter imagens para escala de cinza
- Analisar histogramas de intensidade
- Ajustar brilho e contraste
- Equalizar histogramas para melhorar a qualidade visual
- Calcular métricas de brilho e contraste antes e depois de cada transformação
- Segmentar objetos, detectar e delimitar regiões e contar objetos

---

## 🗂️ Estrutura do Projeto

```
📦 projeto-visao-computacional/
├── funcoes.py       # Módulo com todas as funções de processamento de imagem
├── main.py          # Script principal que executa o pipeline completo
└── README.md
```

---

## ⚙️ Funções Implementadas (`funcoes.py`)

| Função | Descrição |
|---|---|
| `load_image(path)` | Carrega uma imagem a partir de um caminho de arquivo |
| `convert_2_gray(image)` | Converte a imagem para escala de cinza |
| `show_image(image, title)` | Exibe a imagem utilizando Matplotlib |
| `plot_histogram(image, title)` | Plota o histograma de intensidade de pixels |
| `adjust_brightness_contrast(image, alpha, beta)` | Ajusta brilho (`beta`) e contraste (`alpha`) |
| `equalize_image(image)` | Equaliza o histograma para melhorar o contraste global |
| `calculate_metrics(image)` | Retorna o brilho médio e o contraste (desvio padrão) |

---

## 🔄 Pipeline de Execução (`main.py`)

```
Carregar imagem
      ↓
Converter para escala de cinza
      ↓
Exibir imagem + histograma original
      ↓
Calcular métricas originais (brilho e contraste)
      ↓
Ajustar brilho (β=30) e contraste (α=1.3)
      ↓
Exibir imagem ajustada + histograma
      ↓
Calcular métricas pós-ajuste
      ↓
Equalizar histograma
      ↓
Exibir imagem equalizada + histograma
      ↓
Calcular métricas pós-equalização
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **OpenCV (`cv2`)** — processamento e manipulação de imagens
- **Matplotlib** — visualização de imagens e histogramas

---

## 📦 Instalação das Dependências

```bash
pip install opencv-python matplotlib
```

---

## ▶️ Como Executar

1. Clone ou baixe o repositório.
2. Adicione a imagem desejada na raiz do projeto.
3. No arquivo `main.py`, atualize o nome do arquivo de imagem na chamada `load_image(...)`.
4. Execute o script principal:

```bash
python main.py
```

---

## 📊 Exemplo de Saída no Terminal

```
Shape imagem colorida: (1080, 1920, 3)
Shape imagem grayscale: (1080, 1920)

--- MÉTRICAS ORIGINAIS ---
Brilho médio:  127.43
Contraste (desvio padrão):  52.18

--- MÉTRICAS APÓS AJUSTE ---
Brilho médio:  181.20
Contraste (desvio padrão):  67.83

--- MÉTRICAS APÓS EQUALIZAÇÃO ---
Brilho médio:  127.89
Contraste (desvio padrão):  73.41
```

---

## 📝 Observações

- A imagem deve estar no mesmo diretório do script ou o caminho completo deve ser fornecido.
- O parâmetro `alpha` em `adjust_brightness_contrast` controla o **contraste** (valores > 1.0 aumentam o contraste).
- O parâmetro `beta` controla o **brilho** (valores positivos clareiam, negativos escurecem).
- A equalização de histograma redistribui as intensidades para maximizar o contraste global da imagem.
