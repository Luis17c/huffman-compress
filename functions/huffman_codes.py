def generate_huffman_codes(root):
    codes = {}

    def generate_codes_helper(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
        generate_codes_helper(node.left, current_code + "0")
        generate_codes_helper(node.right, current_code + "1")

    generate_codes_helper(root, "")
    return codes


def encode_text(text, codes):
    encoded = ""
    for char in text:
        encoded += codes[char]
    return encoded


def decode_text(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root
    return ''.join(decoded_text)