#unlock the secret message by getting the min number in each demension 
code = ([65,74,66,68,73],[74,96,116,68,80,])


def message3():

    i = 0
    j = 0
    miny = 1000
    minx = 1000
    ans = []

    while i < len(code):
        j = 0
        minx = 1000
        while j < len(code[0]):
            if code[i][j] < minx:
                minx = code[i][j]
            if j == len(code[0]) - 1:
                ans.append(chr(minx))
            j += 1

        i += 1

    print(ans[0] + ans[1])
    return ans