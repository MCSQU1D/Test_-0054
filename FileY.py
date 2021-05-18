import random
import time

stringo = "The quick brown fox jumped over the lazy dog"
stringy = "the dumb cat and"

def Extract(Start, Finish, Extractstring):
    Temp = ""
    Position = Start
    while Position <= Finish:
        Temp = Temp + Extractstring[Position]
        Position += 1
    return Temp

#print(Extract(0,31,stringo))

def Delete(Start,Finish,DeleteString):
    Temp = Extract(0,Start-1,DeleteString)
    Length = len(DeleteString)-1
    Temp = Temp + Extract(Finish+1,Length,DeleteString)
    return Temp


#print(Delete(0,31,stringo))


def Insert(Start,InsertString,MainString):
    Temp = Extract(0,Start-1,MainString)
    Temp = Temp + InsertString
    Length = len(MainString) -1
    Temp = Temp + Extract(Start,Length,MainString)
    return Temp

#print(Insert(31,stringy,stringo))

def RandomArray(min, max, num):
    rNum = []
    arr = []
    for i in range(max-min):
        rNum.append(i + min)
    for i in range(num - 1):
        r = random.randrange(i, max-min)

        arr.append(r)
        rNum[r] = rNum[i]
    return arr

#print(RandomArray(0,10,6))
str = "The cat sat on the mat"

print(Insert(5,"dog",Delete(5,11,Extract(5,18,str))))
