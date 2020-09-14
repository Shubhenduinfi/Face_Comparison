
"""
PyCharm Editor

Created on Set Sep 12 12:54:50 2020

@author: Shubhendu
"""


#IMPORTING LIBERARY'S
'--------------------------'
import cv2
import face_recognition
import tkinter as tk
from tkinter import filedialog


#File Extraction and condition
'------------------------------'
root = tk.Tk()
root.withdraw()

PASSPORT = filedialog.askopenfilename()          #to take Passport image from user
SELFIE= filedialog.askopenfilename()            #to take Selfie from user
TOLARANCE = 0.6                                 #for accuracy
height = 400
width = 400

print(PASSPORT)                                #Showing selected Passport file location
print(SELFIE)                                  #Showing selected Selfie file location



#loading Passport image and converting color from BGR(Blue, Green, Red) to RBG(Red, Blue, Green)
imgPass = face_recognition.load_image_file(PASSPORT)
imgPass = cv2.cvtColor(imgPass, cv2.COLOR_BGR2RGB)
imgPass=cv2.resize(imgPass,(height,width))


#loading Selfie image and converting color from BGR(Blue, Green, Red) to RBG(Red, Blue, Green)
imgSelf = face_recognition.load_image_file(SELFIE)
imgSelf = cv2.cvtColor(imgSelf, cv2.COLOR_BGR2RGB)
imgSelf=cv2.resize(imgSelf,(height,width))


#Processing part or Training part for Passport input
facelocPass = face_recognition.face_locations(imgPass)       #locating face by predefine code
if len(facelocPass) > 0:                                     #to check it detect face or not
    facelocPassport = facelocPass[0]
else:
   print("No faces found in the Passport!")
   quit()
encodingPass = face_recognition.face_encodings(imgPass)[0]                             #Encoding face to compare with other

cv2.rectangle(imgPass,(facelocPassport[3],facelocPassport[0]),(facelocPassport[1],facelocPassport[2]),(0,255,0),2)            #creating Rectangle on detected face


#Processing part or Training part for Selfie input
facelocSelf = face_recognition.face_locations(imgSelf)                  #locating face by predefine code
if len(facelocSelf) > 0:
    facelocSelfie = facelocSelf[0]
else:
    print("No faces found in the Selfie!")
    quit()

encodingSelf = face_recognition.face_encodings(imgSelf)[0]                                              #Encoding face to compare with other
cv2.rectangle(imgSelf,(facelocSelfie[3],facelocSelfie[0]),(facelocSelfie[1],facelocSelfie[2]),(0,255,0),2)        #creating Rectangle on detected face




results = face_recognition.compare_faces([encodingPass],encodingSelf, TOLARANCE)         #Comparing Passport with Selfie image
faceDis = face_recognition.face_distance([encodingPass],encodingSelf)                                 #using face_distance to check the accuracy score
print(results,faceDis)                                                                              #output


#OUTPUT Section

cv2.putText(imgSelf, f'{results}{round(faceDis[0],1)}',(50,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)          #To show accuracy on output Selfie image
cv2.imshow('Passport',imgPass)                                                                        #Showing Sassport
cv2.imshow('Selfie',imgSelf)                                                                               #Showing Selfie
cv2.waitKey(0)                                                                                            #To stop output for infinite time period. which end by clicking q