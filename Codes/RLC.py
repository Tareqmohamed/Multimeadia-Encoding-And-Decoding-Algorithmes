from numpy import array

# with open("text.txt", "w") as f:
#     f.write("aaaaaaaabbbbbccc")

# with open("text.txt", "r") as f:
#     x = f.read()


def run_length_encoding(data):
    # output = ""
    # currunt = x[0]
    # count = 0
    # for i in range(len(x)-1):
    #     if currunt == x[i]:
    #         count += 1
    #     else:
    #         output += str(currunt)
    #         output += str(count)
    #         count = 1
    #         currunt = x[i + 1]
    # count += 1
    # output += str(currunt)
    # output += str(count)
    # return output
    encoded = ""
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded += str(data[i - 1])
            encoded += str(count)
            count = 1

    encoded += str(data[-1])
    encoded += str(count)

    return encoded


def rev_fun(var):
    full_len = ""
    for i in range(len(var) - 1):
        if i % 2 != 0:
            continue
        for n in range(int(var[i + 1])):
            full_len += var[i]
    return full_len
    # print(full_len)


# rev_fun()
# print(run_length_encoding("hello"))
