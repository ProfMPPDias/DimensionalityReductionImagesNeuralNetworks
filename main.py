import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os


# Carrega e verifica a existencia do arquivo JPEG no local, converte a imagem para RGB, redimensiona a imagem pelo pixel.
def load_jpg(file_path):
    if not os.path.exists(file_path):
        raise ValueError("O arquivo fornecido não existe.")

    image = Image.open(file_path)
    image = image.convert("RGB")  # Garante que está em RGB
    width, height = image.size
    pixels = np.array(image)

    return pixels, width, height


# Converte para Tons de Cinza
def convert_to_grayscale(image):
    return np.array(
        [[int(0.299 * r + 0.587 * g + 0.114 * b) for r, g, b in row]
         for row in image])


# Converte para Binária
def binarize_image(image, threshold=127):
    return np.array([[255 if pixel > threshold else 0 for pixel in row]
                     for row in image])


# Função para plotar a imagem na tela
def display_image(image, title):
    plt.imshow(image, cmap='gray' if len(image.shape) == 2 else None)
    plt.title(title)
    plt.axis('off')
    plt.show()


def main():
    file_path = "larissa_manoela.jpg"  # Substitua pelo caminho do seu arquivo JPG

    # Carregar a imagem
    original_image, width, height = load_jpg(file_path)

    # Converter para tons de cinza
    grayscale_image = convert_to_grayscale(original_image)

    # Converter para imagem binária
    binary_image = binarize_image(grayscale_image)

    # Exibir imagens
    display_image(original_image, "Imagem Original")
    display_image(grayscale_image, "Imagem em Tons de Cinza")
    display_image(binary_image, "Imagem Binária")


if __name__ == "__main__":
    main()
