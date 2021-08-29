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



Reaction_Dict = {}
Reaction_Information = LoadInformation("chemicalreaction.txt")
Reaction_Information.pop(0)
for i in Reaction_Information:
    j = i.split("|")
    j_dict = {}
    j_dict["Reactant_1"] = j[0]
    j_dict["Reactant_1_Quantity"] = int(j[1])
    j_dict["Reactant_2"] = j[2]
    j_dict["Reactant_2_Quantity"] = int(j[3])
    j_dict["Resultant"] = j[4]
    j_dict["Resultant_Quantity"] = int(j[5])
    j_dict["Temp_Required"] = float(j[6])
    j_dict["Temp_Added"] = float(j[7])
    Reaction_Dict[j[4]] = j_dict

print(Reaction_Dict)
