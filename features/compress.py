from implementations.huffman_tree import build_huffman_tree
from functions.huffman_codes import generate_huffman_codes, encode_text
from functions.file_operations import read_file, save_huffman_file

def compress():
    folder = 'archives/'
    input_file = "entrada.txt"
    output_file = "saida.huf"

    text = read_file(folder + input_file)

    root = build_huffman_tree(text)

    codes = generate_huffman_codes(root)

    encoded_text = encode_text(text, codes)

    save_huffman_file(root, encoded_text, folder + output_file)

    print("Compressão concluída!")
    print("Texto comprimido salvo em:", folder + output_file)

    return root, codes, encoded_text