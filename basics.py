import cv2
import numpy as np
import face_recognition

imgHamza=face_recognition.load_image_file("./Images/hamza.JPG")
imgHamza=cv2.cvtColor(imgHamza, cv2.COLOR_BGR2RGB)
#imgHamza=cv2.resize(imgHamza,(1000,800))
imgHamzaTest=face_recognition.load_image_file("./Images/hamzaTest.jpg")
imgHamzaTest=cv2.cvtColor(imgHamzaTest,cv2.COLOR_BGR2RGB)



faceloc=face_recognition.face_locations(imgHamza)[0]
encodeHamza=face_recognition.face_encodings(imgHamza)[0]
cv2.rectangle(imgHamza, (faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(234,8,9),4)

facelocTest=face_recognition.face_locations(imgHamzaTest)[0]
encodeHamzaTest=face_recognition.face_encodings(imgHamzaTest)[0]
cv2.rectangle(imgHamzaTest, (facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(234,8,9),4)


cv2.imshow("Image2",imgHamzaTest)
cv2.imshow('Image' , imgHamza)

cv2.waitKey(0)
