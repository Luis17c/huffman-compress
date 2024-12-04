from functions.frequency_count import frequencyCount

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = frequencyCount(text)

    nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]