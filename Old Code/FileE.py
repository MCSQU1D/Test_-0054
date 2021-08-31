import numpy as np

Atom_Array = np.array([])

arrayCreate = False
arrx = np.array([])
a = 0
for i in range(890):
    for x in range(490):
        arrx = np.append(arrx, "null")
    a += 1
    per_done = round(a/890 * 100)
    print(str(per_done) +"%")


Atom_Array = arrx.reshape(490,890)

print(Atom_Array)


    #print(list)

#arrx = np.array([0,1,2,3])
#arry = np.array(["a","b","c","d"])

#arrz = np.stack((arrx, arry), axis=0)
