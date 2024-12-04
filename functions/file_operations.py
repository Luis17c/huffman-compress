import json

from functions.huffman_tree_operations import deserialize_huffman_tree, serialize_huffman_tree

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def save_huffman_file(tree, encoded_text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump({"tree": serialize_huffman_tree(tree), "data": encoded_text}, f)

def load_huffman_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        huf_data = json.load(f)
    tree = deserialize_huffman_tree(huf_data['tree'])
    encoded_text = huf_data['data']
    return tree, encoded_text