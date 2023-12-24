def countfrq(msg):
    c = {}
    for i in msg:
        c[i] = msg.count(i)
    sorted_c = sorted(c.items(), key=lambda x: x[1], reverse=1)
    print("-------------------------------------VLC--------------------------------")
    print('The freq of "', msg, '":', sorted_c)
    return sorted_c


def generate_code(x):
    a = []

    for i in x:
        list1 = ["1"]
        if x.index(i) != len(x) - 1:
            b = list1 * x.index(i) + ["0"]
        else:
            b = list1 * x.index(i)
        a += (i[0], str(b))

    print("The table :         ", a)
    return a


def VLC_encode(word):
    frq = countfrq(word)
    table = generate_code(frq)
    code = ""
    for j in range(0, len(word)):
        for i in range(0, len(table), 2):
            if word[j] == table[i]:
                code += str(table[i + 1])

    strcoded = strcode(code)
    print("The encoded word:   ", strcoded)
    print("------------------------------------------------------------------------")
    return strcoded, frq


def strcode(code):
    str_code = ""
    for i in range(0, len(code)):
        if (
            code[i] == "["
            or code[i] == "]"
            or code[i] == "'"
            or code[i] == '"'
            or code[i] == ","
            or code[i] == " "
        ):
            continue
        else:
            str_code += code[i]
    return str_code


def decode(code, table):
    # strtable=strcode(table)
    key = []
    value = []
    for i in range(0, len(table), 2):
        key.append(table[i])
        value.append(strcode(table[i + 1]))

    dicttable = dict(zip(value, key))

    start = 0
    word = ""
    for i in range(0, len(code) + 1):
        if code[start:i] in dicttable:
            word += dicttable[code[start:i]]
            start = i
    return word
    # print("Decoded word:       ", word)


# frq = countfrq("hello")

# code = VLC_encode("hello")

# # # encode(msg,generate_code(countfrq(msg)))
# vlaue = [
#     "l",
#     "['0']",
#     "h",
#     "['1', '0']",
#     "e",
#     "['1', '1', '0']",
#     "o",
#     "['1', '1', '1']",
# ]
# print(decode("1011000111", vlaue))
