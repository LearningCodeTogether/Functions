#unlock the secret message by getting the max number in each demension 

code = ([65,74,66,68,70],[74,96,68,80,117],[104,106,78,80,115],[116,74,96,68,80])
def message1():
    answer = ""

    z = 0

    for z in range(len(code)):
        x = 0
        y = 4
        while x != y:
            if code[z][x]<code[z][y]:
             x = x + 1

            elif code[z][x]>code[z][y]:
              y = y - 1
        letter = chr(code[z][x])
        answer = answer + letter
        # print(code[z][x], "is the greatest value"
        z = z + 1

    print(answer)

