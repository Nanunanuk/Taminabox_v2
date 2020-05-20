import os
import pickle

folderPath='/home/pi/pi-share/'

with open(folderPath+'LiederDatenbank.txt', "rb") as fp:   
	lib = pickle.load(fp)

for x in lib.keys():
	print(x)
	print(lib[x])

print(len(lib[x]))
fp.close()
