from implementations.huffman_tree import HuffmanNode

def deserialize_huffman_tree(tree_data):
    if tree_data is None:
        return None
    node = HuffmanNode(tree_data['char'], tree_data['freq'])
    node.left = deserialize_huffman_tree(tree_data['left'])
    node.right = deserialize_huffman_tree(tree_data['right'])
    return node

def serialize_huffman_tree(node):
    if node is None:
        return None
    return {
        "char": node.char,
        "freq": node.freq,
        "left": serialize_huffman_tree(node.left),
        "right": serialize_huffman_tree(node.right)
    }