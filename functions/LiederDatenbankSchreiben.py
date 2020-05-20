# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:18:48 2019

@author: Nils
"""

import pickle
import os

def is_empty_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def create_songList(folderPath):
    folder=raw_input("Bitte Ordnername eingeben!")
    b =folderPath+folder
    songList=sorted(os.listdir(b))
        
    # Deleting entries that are not mp3
    newList=[]
    for i in range(len(songList)):
        if '.mp3' in songList[i]:
            newList.append(songList[i])
    songList=newList
    return folder, songList

folderPath='/home/pi/pi-share/'

if is_empty_file(folderPath+'LiederDatenbank.txt')==False:
    folder, songList=create_songList(folderPath)
    with open(folderPath +'LiederDatenbank.txt', "wb") as fp:  
        pickle.dump({folder:songList}, fp)
    fp.close()
    
else:
    with open(folderPath+'LiederDatenbank.txt', "rb") as fp:   
        lib = pickle.load(fp)
        
    folder, songList=create_songList(folderPath)
    lib.update({folder:songList})
    
    with open(folderPath +'LiederDatenbank.txt', "wb") as fp:  
        pickle.dump(lib, fp) 
    fp.close()
