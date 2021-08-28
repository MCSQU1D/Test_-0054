import pygame
from time import sleep
from time import perf_counter
import random
import os
import math
import threading
from operator import itemgetter, attrgetter

Atom_Dict = {}

def LoadInformation(file):
    path = os.path.join("files")
    filelist = []

    for r, d, f in os.walk(path):
        for file_finder in f:
            if '.txt' in file_finder:
                filelist.append(file_finder)
    for i in filelist:
        if i == file:
            file_finder = i

    file_pathname = os.getcwd()+"/files/" +file
    file_opened = open(file_pathname,"r")
    file_split = file_opened.read().split("\n")
    return file_split



Reaction_Information = LoadInformation(chemicalreaction)
print(Reaction_Information)
