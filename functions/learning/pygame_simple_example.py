# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:28:39 2019

@author: Nils
"""

import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("C:/Users/Nils/Music/Buena Vista Social Club/01 Chan Chan.mp3")
pygame.mixer.music.play()
x=0
while x<5:
    time.sleep(1)
    x=x+1
pygame.mixer.music.stop()
