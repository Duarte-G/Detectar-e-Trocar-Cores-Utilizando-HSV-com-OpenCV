# Detectar-e-Trocar-Cores-Utilizando-HSV-com-OpenCV
O código utiliza a biblioteca OpenCV para capturar imagens da câmera e processá-las no espaço de cor HSV. O processo envolve os seguintes passos:

- **Captura e Conversão:**
A imagem capturada da câmera é convertida para HSV.

- **Criação de Máscaras:**
Máscaras são criadas para identificar cores específicas (vermelho, azul e verde). Cada máscara é gerada usando limites definidos para Matiz (Hue), Saturação (Saturation) e Valor (Value) da cor desejada.

- **Aplicação de Máscaras:**
As máscaras são aplicadas à imagem original para extrair as áreas correspondentes a cada cor

- **Substituição de cores:**
- Cada cor detectada foi substituída por uma nova cor (vermelho trocado por verde, azul pelo vermelho e verde por azul). A substituição é realizada criando imagens substitutas para cada cor detectada.

O código realiza a detecção de cores, aplica a substituição e exibe a imagem permitindo observar a troca de cores em tempo real.

## Como Usar
 - Clone o repositório para sua máquina local.
 - Instale as bibliotecas necessárias no código.
 - Ligue a câmera que será utilizada.
 - Execute o .ipynb para explorar o código e resultados.
 - Sinta-se à vontade para alterar o código para utilizar outras cores ou realizar outras conversões.
