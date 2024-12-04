import json

from functions.huffman_tree_operations import deserialize_huffman_tree, serialize_huffman_tree

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def save_huffman_file(tree, encoded_text, file_path):
    with open(file_path, 'wb') as f:
        tree_data = serialize_huffman_tree(tree)
        tree_bytes = json.dumps(tree_data).encode('utf-8')

        f.write(len(tree_bytes).to_bytes(4, 'big'))
        f.write(tree_bytes)

        encoded_bytes = int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, 'big')
        f.write(encoded_bytes)

def load_huffman_file(file_path):
    with open(file_path, 'rb') as f:
        tree_size = int.from_bytes(f.read(4), 'big')

        tree_bytes = f.read(tree_size)
        tree_data = json.loads(tree_bytes.decode('utf-8'))
        tree = deserialize_huffman_tree(tree_data)

        encoded_bits = bin(int.from_bytes(f.read(), 'big'))[2:]
        return tree, encoded_bits