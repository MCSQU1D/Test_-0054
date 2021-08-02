class Data:
    pass

myList = []

for i in range(20):
    data = Data()
    data.n = 3
    data.n_squared = i * i
    myList.append(data)


def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

if contains(myList, lambda x: x.n == 3):  # True if any element has .n==3
    # do stuff
    print("lmao")
