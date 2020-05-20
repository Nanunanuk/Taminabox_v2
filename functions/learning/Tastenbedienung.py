# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:12:12 2019

@author: Nils
"""

import os
import pygame


myDir='C:/Users/Nils/Music/Buena Vista Social Club'
cardList=['1','2','3']
card=input("Bitte Karte auflegen!")



if any(card in s for s in cardList):

    
        
    songs=os.listdir(myDir)
    
    pygame.mixer.init()
    pygame.mixer.music.load(myDir+'/'+songs[0])
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy()==True:
        eingabe = input("Ihre Eingabe? ")
        if eingabe=='s':
            pygame.mixer.music.stop()
        if eingabe=='p':
            pygame.mixer.music.pause()
        if eingabe=='u':
            pygame.mixer.music.unpause()    
        if eingabe=='f':
            pygame.mixer.music.load(myDir+'/'+songs[0])
            pygame.mixer.music.play()
        continue


