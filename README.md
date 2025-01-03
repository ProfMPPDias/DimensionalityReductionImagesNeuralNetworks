# Redução de Dimensionalidade em Imagens para Redes Neurais

Este projeto realiza o processamento básico de uma imagem JPEG, incluindo a conversão para tons de cinza e binarização. Ele utiliza as bibliotecas Python `matplotlib`, `numpy` e `Pillow` para manipulação e visualização das imagens.

## Funcionalidades
- Carregamento de uma imagem JPEG e verificação de sua existência.
- Conversão da imagem para tons de cinza.
- Binarização da imagem com base em um valor de limiar.
- Exibição das imagens processadas.

## Pré-requisitos
Certifique-se de ter o Python 3.7 ou superior instalado em sua máquina.

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/ProfMPPDias/DimensionalityReductionImagesNeuralNetworks.git
   cd DimensionalityReductionImagesNeuralNetworks
   ```

2. Instale as bibliotecas necessárias:
   ```bash
   pip install matplotlib numpy pillow
   ```

## Como Usar
1. Coloque a imagem que deseja processar no mesmo diretório do código e renomeie-a para `larissa_manoela.jpg` ou ajuste o caminho do arquivo na função `main`.

2. Execute o script:
   ```bash
   python main.py
   ```

3. As imagens processadas serão exibidas em janelas separadas:
   - Imagem original.
   - Imagem em tons de cinza.
   - Imagem binária.

## Estrutura do Código
- `load_jpg(file_path)`: Carrega e converte uma imagem para RGB.
- `convert_to_grayscale(image)`: Converte a imagem para tons de cinza.
- `binarize_image(image, threshold)`: Converte a imagem em tons de cinza para uma imagem binária com base em um limiar.
- `display_image(image, title)`: Exibe a imagem com um título especificado.

## Exemplo de Saída
1. Imagem Original:
   ![Imagem Original](https://github.com/ProfMPPDias/DimensionalityReductionImagesNeuralNetworks/blob/main/Original.jpeg)
2. Imagem em Tons de Cinza:
   ![Imagem Tons de Cinza](https://github.com/ProfMPPDias/DimensionalityReductionImagesNeuralNetworks/blob/main/Greyscale.jpeg)
3. Imagem Binária:
   ![Imagem Binária](https://github.com/ProfMPPDias/DimensionalityReductionImagesNeuralNetworks/blob/main/Binary.jpeg)

## Contribuição
Sinta-se à vontade para contribuir com este projeto! Faça um fork, implemente suas melhorias e envie um pull request.

## Licença
Este projeto é licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
