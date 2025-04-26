# Face Detection

This code is created on PyCharm IDE.
In this user can provide passport image which stores in Passport using tkinter liberary.
and after that user have to select another selfi to compare. that it match or not(this was my condition to provide both as input other wise you can add directory where image are save to train by using for loop.)

After getting file manually loading image and convert it from BGR to RBG and resize to get specific size outpout. doing this for both Passport and Selfie image.
now Locating face and giving condition if find then run else quit. and encoding image for Passport and same processes for Selfie.

training is done. its time to give output for this first we comparing both encoding of Passport and Selfie with some tolarence. and palcing accuracy by face_distance.

now in end showing output with some conditions.
