def LZ77_search(search, look_ahead):
    ls = len(search)
    llh = len(look_ahead)

    if ls == 0:
        return (0, 0, look_ahead[0])

    if (llh) == 0:
        return (-1, -1, "")

    best_length = 0
    best_offset = 0
    buf = search + look_ahead

    search_pointer = ls
    # print( "search: " , search, " lookahead: ", look_ahead)
    for i in range(ls - 1, -1, -1):
        length = 0
        while buf[i + length] == buf[search_pointer + length]:
            length = length + 1
            if search_pointer + length == len(buf):
                length = length - 1
                break
            if i + length >= search_pointer:
                break
        if length > best_length:
            best_offset = i
            best_length = length

    return (best_offset, best_length, buf[search_pointer + best_length])


# *********************************************
# *********************************************
def code_LZ77(input):
    searchiterator = 0
    lhiterator = 0
    result = []
    while lhiterator < len(input):
        search = input[searchiterator:lhiterator]
        look_ahead = input[lhiterator : len(input)]

        [offset, length, char] = LZ77_search(search, look_ahead)
        if length != 0:
            offset = lhiterator - offset

        result += [[offset, length, char]]

        # print (offset, length, char)

        lhiterator = lhiterator + length + 1

    return result


# x="hello"
# output=code_LZ77(x)
# print(output)


def decode_LZ77(code):
    chararray = ""
    for offset, length, char in code:
        if (offset == 0) and (length == 0):
            chararray += char
        else:
            chararray += (
                chararray[len(chararray) - offset : len(chararray) - offset + length]
                + char
            )
    return list(chararray)


# output2=decode_LZ77(output)
# print(output2)


def TotalGain(the_data, coding):
    # afterCompression = os.path.getsize("a.txt")
    # beforeCompression = os.path.getsize("b.txt")

    beforeCompression = len(the_data) * 8
    afterCompression = 3 * len(coding) * 8
    CR = beforeCompression / afterCompression
    # print("Space usage before compression (in bits):", beforeCompression)
    # print("Space usage after compression (in bits):", afterCompression)
    # print("CR=",CR)


# print(len(output))
# TotalGain(x, output)
