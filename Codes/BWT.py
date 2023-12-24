def encode(input):
    assert "%" not in input
    input = input + "%"

    table = [input[i:] + input[:i] for i in range(len(input))]

    table = sorted(table)

    last_column = [row[-1:] for row in table]
    bwt = "".join(last_column)
    return bwt


def decode(bwt):
    table = [""] * len(bwt)

    for i in range(len(bwt)):
        table = [bwt[i] + table[i] for i in range(len(bwt))]
        table = sorted(table)

    inverse_bwt = [row for row in table if row.endswith("%")][0]

    inverse_bwt = inverse_bwt.rstrip("%")

    print("decode:", inverse_bwt)
    return inverse_bwt
