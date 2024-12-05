# Compressão e Descompressão com Huffman

Este projeto implementa um sistema de compressão e descompressão de arquivos de texto utilizando o algoritmo de Huffman. Ele permite compactar textos para reduzir seu tamanho e, posteriormente, descompactá-los para recuperar o conteúdo original.

## Estrutura do Projeto

**/archives**

- `entrada.txt`: Arquivo de entrada (texto original a ser compactado)
- `saida.huf`: Arquivo comprimido gerado

**/features**

- `compress.py`: Função para compactar texto
- `decompress.py`: Função para descompactar texto

**/functions**

- `file_operations.py`: Funções de leitura, escrita e manipulação de arquivos
- `frequency_count.py`: Função para contar frequências de caracteres
- `huffman_codes.py`: Funções para geração de códigos e decodificação
- `huffman_tree_operations.py`: Operações com árvore de Huffman

**/implementations**

- `huffman_tree.py`: Construção da árvore de Huffman

**Arquivos principais**

- `index.py`: Script principal com menu interativo (CLI)
- `interface.py`: Interface gráfica para compressão e descompressão (GUI)

## Requisitos

- **Python 3.6+**
- **Bibliotecas utilizadas**:
  - Para a **interface CLI (index.py)**: Nenhuma biblioteca externa é necessária. Apenas as bibliotecas padrão do Python são utilizadas.
  - Para a **interface GUI (interface.py)**: As seguintes bibliotecas são necessárias:
    - `tkinter` (padrão no Python)
    - `subprocess` (padrão no Python)
    - `sys` (padrão no Python)
    - `os` (padrão no Python)
  - Caso alguma biblioteca esteja faltando, o script **interface.py** realiza a instalação automática.

## Como Usar

### 1. Configurar o Ambiente
Certifique-se de que o diretório contém a estrutura de arquivos listada acima e que o Python está instalado.

### 2. Compactar um Texto
1. O texto que deseja compactar pode ser editado no arquivo `archives/entrada.txt`.
2. Para compactar, utilize uma das opções:
   - **Interface CLI**: Execute o comando:
     ```bash
     python index.py
     ```
     No menu interativo, selecione `1` para compactar.
   - **Interface GUI**: Execute o comando:
     ```bash
     python interface.py
     ```
     Siga as instruções da interface gráfica.

### 3. Descompactar um Texto
1. O texto que deseja descompactar deve estar no arquivo `archives/saida.huf`, incluindo a árvore de Huffman no formato serializado.
2. Para descompactar, utilize uma das opções:
   - **Interface CLI**: Execute o comando:
     ```bash
     python index.py
     ```
     No menu interativo, selecione `2` para descompactar.
   - **Interface GUI**: Execute o comando:
     ```bash
     python interface.py
     ```
     Siga as instruções da interface gráfica.

## Funcionalidades

### Compressão
- Reduz o tamanho de arquivos de texto utilizando a codificação de Huffman.
- Gera um arquivo `.huf` contendo a árvore serializada e o texto compactado.

### Descompressão
- Restaura o texto original a partir do arquivo `.huf` compactado.
- Recria o texto original no arquivo `archives/entrada.txt`.

## Estrutura da Árvore de Huffman no Arquivo Compactado
O arquivo `.huf` contém:
1. **Árvore de Huffman Serializada**: Utilizada para decodificar o texto compactado.
2. **Texto Compactado**: Representação binária comprimida do texto original.

## Observações Adicionais
- O projeto oferece duas opções de uso: CLI e GUI, acessíveis pelos scripts `index.py` e `interface.py`.
- Os arquivos de entrada e saída são manipulados nos diretórios:
  - Entrada: `archives/entrada.txt`
  - Saída: `archives/saida.huf`
