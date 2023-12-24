inp = "aaabbbc"


def code_lzw(inp):
    dic = {}
    for i in inp:
        if i not in dic:
            dic[i] = str(len(dic))
    output = ""
    out = ""
    comp = ""
    data = ""
    size = len(dic)
    for data in inp:
        output = out + data
        if output in dic:
            out = output
        else:
            comp += dic[out]
            out = data
            dic[output] = str(size)
            size += 1
    if data in dic:
        comp += dic[out]
    print(
            "-------------------------------------LZW--------------------------------"
        )
    print("The table of :",inp,":", dic)

    print("The encoded word: ", comp)
    print("------------------------------------------------------------------------")
    return comp


def decode_lzw(compressed_data, dictionary):
    decompressed_data = ""
    string = ""
    next_code = len(dictionary)
    for code in compressed_data:
        if not (code in dictionary.values()):
            dictionary[string + (string[0])] = str(code)
        decompressed_data += list(dictionary.keys())[
            list(dictionary.values()).index(code)
        ]
        if not (len(string) == 0):
            dictionary[
                string
                + (list(dictionary.keys())[list(dictionary.values()).index(code)][0])
            ] = str(next_code)
            next_code += 1
        string = list(dictionary.keys())[list(dictionary.values()).index(code)]
    print("decompressed_data", decompressed_data)
    print("dictionary after decompressed", dictionary)

    return decompressed_data
# coding = code_lzw(dictionary)
# inp = "ababababaccabc"
# dictionary = {}
# for i in inp:
#     if i not in dictionary:
#         dictionary[i] = str(len(dictionary))
# print(dictionary)
# decode_lzw(coding, dictionary)


# def TotalGain(the_data, coding):
#     # afterCompression = os.path.getsize("a.txt")
#     # beforeCompression = os.path.getsize("b.txt")

#     beforeCompression = len(the_data) * 8
#     afterCompression = len(coding) * 8
#     CR = beforeCompression / afterCompression
#     print("Space usage before compression (in bits):", beforeCompression)
#     print("Space usage after compression (in bits):", afterCompression)
#     print("CR=", CR)


# TotalGain(inp, coding)
