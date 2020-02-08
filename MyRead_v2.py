#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import pickle
import os
import pygame
import time
import RPi.GPIO as GPIO

pygame.mixer.init()



GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # forward
GPIO.add_event_detect(10, GPIO.RISING,bouncetime=500)  # forward
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # backward
GPIO.add_event_detect(12, GPIO.RISING,bouncetime=500)  # backward
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # play/pause
GPIO.add_event_detect(8, GPIO.RISING,bouncetime=500)  # play/pause

continue_reading = True

# Reading in Album database
folderPath='/home/pi/pi-share/'
with open(folderPath+'LiederDatenbank.txt', "rb") as fp:   
	lib = pickle.load(fp)
    
# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print("Welcome to the MFRC522 data read example")
print("Press Ctrl-C to stop.")

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
previousAlbum=""
noCount=0
cardDetected=False
songNr=0
songRunning=True

while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    #if status == MIFAREReader.MI_OK:
    #    print("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        #print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            data=MIFAREReader.MFRC522_Read(8)
            text="".join(chr(x) for x in data)
            
            noCount=0
            
            if cardDetected==False:
                
                cardDetected=True
                for albumKey in lib.keys():
                    if albumKey in text:
                        songNr=0
                        currentAlbum=albumKey
                        pygame.mixer.music.load(folderPath + albumKey + '/' + lib[albumKey][songNr])
                        pygame.mixer.music.play() 
                        print(albumKey + ' is playing')
                        
            
            
            
                
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print("Authentication error")
    else:
        noCount=noCount+1
        if noCount>1:
            pygame.mixer.music.stop()
            print('No card!')
            cardDetected=False
    
    if GPIO.event_detected(10):
        print('Button pressed')
        if songNr<len(lib[currentAlbum])-1:
            print('Song ' + str(songNr+2) + ' of ' + str(len(lib[currentAlbum])))
            songNr = songNr+1
            pygame.mixer.music.load(folderPath + currentAlbum + '/' + lib[currentAlbum][songNr])
            pygame.mixer.music.play()

    if GPIO.event_detected(12):
        print('Button pressed')
        if songNr>0:
            print('Song ' + str(songNr) + ' of ' + str(len(lib[currentAlbum])))
            songNr = songNr-1
            pygame.mixer.music.load(folderPath + currentAlbum + '/' + lib[currentAlbum][songNr])
            pygame.mixer.music.play()
            
    if GPIO.event_detected(8):
        print('Button pressed')
        
        if songRunning==True:
            print('Song paused')
            pygame.mixer.music.pause()
            songRunning=False
        else:
            print('Song playing')
            pygame.mixer.music.unpause()
            songRunning=True
