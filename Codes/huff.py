import os.path

with open("huffman_decoding.txt", "w") as f:
    f.write("AAAAAAABBCCCCCCDDDEEEEEEEEE")

with open("huffman_decoding.txt", "r") as f:
    the_data = f.read()


""" A supporting function in order to calculate the probabilities of symbols in specified data """


def CalculateProbability(the_data):
    the_symbols = dict()
    for item in the_data:
        if the_symbols.get(item) == None:
            the_symbols[item] = 1
        else:
            the_symbols[item] += 1
    return the_symbols


""" A supporting function in order to print the codes of symbols by travelling a Huffman Tree """
the_codes = dict()


def CalculateCodes(node, value=''):
    # a huffman code for current node
    newValue = value + str(node.code)

    if (node.left):
        CalculateCodes(node.left, newValue)
    if (node.right):
        CalculateCodes(node.right, newValue)

    if (not node.left and not node.right):
        the_codes[node.symbol] = newValue

    return the_codes


""" A supporting function in order to get the encoded result """


def OutputEncoded(the_data, coding):
    encodingOutput = []
    for element in the_data:
        # print(coding[element], end = '')
        encodingOutput.append(coding[element])

    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string


""" A supporting function in order to calculate the space difference between compressed and non compressed data"""

def TotalGain(the_data, coding):
    #afterCompression = os.path.getsize("huffman_encoding.txt")
    #beforeCompression = os.path.getsize("huffman_decoding.txt")

    # total bit space to store the data before compression
    beforeCompression = len(the_data) * 8
    afterCompression = 0
    the_symbols = coding.keys()
    for symbol in the_symbols:
        the_count = the_data.count(symbol)
        # calculating how many bit is required for that symbol in total
        afterCompression += the_count * len(coding[symbol])
    CR=beforeCompression/afterCompression
    print("Space usage before compression (in bits):", beforeCompression)
    print("Space usage after compression (in bits):", afterCompression)
    print("CR=",CR)



def HuffmanEncoding(the_data):
    symbolWithProbs = CalculateProbability(the_data)
    the_symbols = symbolWithProbs.keys()
    the_probabilities = symbolWithProbs.values()
    print("symbols: ", the_symbols)
    print("probabilities: ", the_probabilities)

    the_nodes = []

    # converting symbols and probabilities into huffman tree nodes
    for symbol in the_symbols:
        the_nodes.append(Nodes(symbolWithProbs.get(symbol), symbol))

    while len(the_nodes) > 1:
        # sorting all the nodes in ascending order based on their probability
        the_nodes = sorted(the_nodes, key=lambda x: x.probability)
        # for node in nodes:
        #      print(node.symbol, node.prob)

        # picking two smallest nodes
        right = the_nodes[0]
        left = the_nodes[1]

        left.code = 0
        right.code = 1

        # combining the 2 smallest nodes to create new node
        newNode = Nodes(left.probability + right.probability, left.symbol + right.symbol, left, right)

        the_nodes.remove(left)
        the_nodes.remove(right)
        the_nodes.append(newNode)

    huffmanEncoding = CalculateCodes(the_nodes[0])
    print("symbols with codes", huffmanEncoding)
    print('the_nodes',the_nodes)
    TotalGain(the_data, huffmanEncoding)
    encodedOutput = OutputEncoded(the_data, huffmanEncoding)
    print("-----------------------------------HUFFMAN------------------------------")

    print("The Tree:   ", huffmanEncoding)
    print("The encoded word:   ", encodedOutput)
    print("------------------------------------------------------------------------")
    return encodedOutput,huffmanEncoding


def HuffmanDecoding(encoded_data,huffman_tree):
    decoded_data = ''
    com = ""
    for i in encoded_data:

        com += i

        if com in huffman_tree.values():
            decoded_data += list(huffman_tree.keys())[list(huffman_tree.values()).index(com)]
            com = ""


    return decoded_data




class Nodes:
    def __init__(self, probability, symbol, left=None, right=None):
        # probability of the symbol
        self.probability = probability

        # the symbol
        self.symbol = symbol

        # the left node
        self.left = left

        # the right node
        self.right = right

        # the tree direction (0 or 1)
        self.code = ''



# encoding, the_tree = HuffmanEncoding(the_data)
# print("encoding",encoding)
# print("tree",the_tree)
# print(type(encoding))
# decoding=HuffmanDecoding(encoding, the_tree)
# with open("huffman_encoding.txt", "w") as f:
#     f.write(encoding)

# with open("huffman_encoding.txt", "r") as f:
#         decode = f.read()



# print("Encoded output", encoding)
# print("Decoded Output", decoding)