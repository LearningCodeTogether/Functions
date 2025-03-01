#unlock the secret message by getting the Min number in each demension 

code = ([68,104,106,78,80],[150,200,111,112,116])



def message2():
    List1 = [68,104,106,78,80]
    Pos1 = 0
    Min1 = 10000
    Answer1 = ""
    while(Pos1<len(List1)):
        if List1[Pos1] < Min1:
            Min1 = List1[Pos1]
        Pos1 += 1
        Answer1 = chr(Min1)
    


    List2 = [150,200,111,112,116]
    Pos2 = 0
    Min2 = 10000
    Answer2 = "?"
    while(Pos2<len(List2)):
        if List2[Pos2] < Min2:
            Min2 = List2[Pos2]
        Pos2 += 1
        Answer2 = chr(Min2)
    print (Answer1+Answer2)