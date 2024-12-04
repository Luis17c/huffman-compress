from functions.huffman_codes import decode_text
from functions.file_operations import write_file, load_huffman_file

def decompress():
    compressed_file = "saida.huf"

    root, encoded_text = load_huffman_file("archives/" + compressed_file)

    decoded_text = decode_text(encoded_text, root)
    
    write_file("archives/entrada.txt", decoded_text)
    print("\nTexto descomprimido salvo em: archives/entrada.txt")
