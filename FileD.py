import threading
import time

def testa():
    print('testa')
    time.sleep(6)
    print("done a")
    return

def testb():
    print('testb')
    testthingofgs = input("Input: ")
    print("done b")
    return

threads = []

a = threading.Thread(target=testa)
threads.append(a)
a.start()

b = threading.Thread(target=testb)
threads.append(b)
b.start()
