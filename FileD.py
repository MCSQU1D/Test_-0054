import numpy
import math



#### [x, y, "Letter"]

#arr = numpy.array([0, 0, "A"])

#for i in range(10):
#    for j in range(10):
#        arr2 = [i, j, "F"]
#        arr = numpy.vstack((arr, arr2))

#while True:
#    for i in arr:
#        if "A" in i:
#            print(i)
#            print("Next")
    #print(i[0] + i[1])

pi = 0.0
for i in range(10000000000):
    pi += 1/((i+1)*(i+1))

print(math.sqrt(pi*6))
