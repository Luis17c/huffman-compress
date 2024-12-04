# Compressão e Descompressão com Huffman

Este projeto implementa um sistema de compressão e descompressão de arquivos de texto utilizando o algoritmo de Huffman. Ele permite compactar textos para reduzir seu tamanho e, posteriormente, descompactá-los para recuperar o conteúdo original.

## Estrutura do Projeto

/archives 
    ├── entrada.txt # Arquivo de entrada (texto original a ser compactado) 
    ├── saida.huf # Arquivo comprimido gerado 
/features 
    ├── compress.py # Função para compactar texto 
    ├── decompress.py # Função para descompactar texto 
/functions 
    ├── file_operations.py # Funções de leitura, escrita e manipulação de arquivos 
    ├── frequency_count.py # Função para contar frequências de caracteres 
    ├── huffman_codes.py # Funções para geração de códigos e decodificação 
    ├── huffman_tree_operations.py # Serialização e desserialização da árvore de Huffman
/implementations 
    ├── huffman_tree.py # Construção da árvore de Huffman
index.py # Script principal com menu interativo

## Requisitos

- **Python 3.6+**

## Como Usar

### 1. Configurar o Ambiente
Certifique-se de que o diretório contém a estrutura de arquivos listada acima e que o Python está instalado.

### 2. Compactar um Texto
1. O texto que deseja compactar pode ser editado no arquivo `archives/entrada.txt`.

2. Execute o comando:
   ```bash
   python index.py
   ```
3. Selecione 1 no menu interativo para compactar

### 3. Descompactar um Texto
1. O texto que deseja descompactar pode ser editado no arquivo `archives/saida.huf`, deve contar a árvore de Huffman no arquivo.

2. Execute o comando:
   ```bash
   python index.py
   ```
3. Selecione 2 no menu interativo para descompactar

## Funcionalidades
### Compressão
Reduz o tamanho de arquivos de texto utilizando a codificação de Huffman.

### Descompressão
Restaura o texto original a partir do arquivo compactado.

### Modularidade
Código organizado em funções e módulos, facilitando a manutenção.

### Limitações
A descompressão requer o arquivo saida.huf contendo a árvore de Huffman embutida.
A compactação e descompactação sobrescrevem os arquivos existentes sem confirmação.

### Estrutura da Árvore de Huffman no Arquivo Compactado
O arquivo .huf contém:
Árvore de Huffman Serializada: Utilizada para decodificar o texto compactado.
Texto Compactado: Representação binária comprimida do texto original.