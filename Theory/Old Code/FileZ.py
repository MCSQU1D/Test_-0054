import random
from time import perf_counter
#UnsortedList = [5,4,3,9,3,5,8,5,3,5,8,3,6,8,5,3,3,5,7,0,9,8,7,6,5,4,3,2,1,2,3,3,4,4,3,69]

global UnsortedList
global UnsortedListb
UnsortedList = []
for i in range(1000):
    UnsortedList.append(random.randrange(0, 100))
UnsortedListb = UnsortedList

def theNumbers():
    global UnsortedList
    Numitems = len(UnsortedList)
    CurrentItem = 1
    #UnsortedList.sort()
    while CurrentItem <= Numitems - 1:
        CurrentDataItem = UnsortedList[CurrentItem]
        Comparison = 0
        Finish = False
        while Comparison < CurrentItem and Finish == False:
            if CurrentDataItem < UnsortedList[Comparison]:
                ShuffleItem = CurrentItem
                while ShuffleItem > Comparison:
                    UnsortedList[ShuffleItem] = UnsortedList[ShuffleItem-1]
                    ShuffleItem = ShuffleItem - 1
                UnsortedList[Comparison] = CurrentDataItem
                Finish = True
            Comparison += 1
            #print(Comparison)
        CurrentItem += 1
    #print(UnsortedList)


def Sorty():
    global UnsortedListb
    UnsortedListb.sort()


list = []
for a in range(50):
    print(a)
    start = perf_counter()
    theNumbers()
    end = perf_counter()
    list.append(end-start)
    #print(end-start)

average = 0

for i in list:
    average += i
average = average/(len(list))
print("Average: " + str(average))


list = []
for a in range(50):
    #print(a)
    start = perf_counter()
    Sorty()
    end = perf_counter()
    list.append(end-start)
    #print(end-start)

average = 0

for i in list:
    average += i
average = average/(len(list))
print("Average: " + str(average))







#Low = 1
#High = len(UnsortedList)
#Found = False
#ItemToFind = 69 #int(input("The Numbers: "))
#while High >= Low and Found == False:
#    Middle = int((Low + High)/2)
#    if ItemToFind < UnsortedList[Middle]:
#        High = Middle - 1
#    elif ItemToFind == UnsortedList[Middle]:
#        Found = True
#    else:
#        Low = Middle + 1
#if Found == True:
#    print("Found")
#else:
#    print("Not found")
#Fount_Number = False
#for i in UnsortedList:
#    if ItemToFind == i:
#        print("Found")
#        Fount_Number = True
#        break
#        #print("Not found")
#    else:
#        Fount_Number = False
#if Fount_Number == False:
#    print("Not found")
