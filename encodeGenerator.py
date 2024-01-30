import cv2
import face_recognition
import os
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
"databaseURL" : "https://facerecognitionrealtime-b1c32-default-rtdb.firebaseio.com/",
"storageBucket" : "facerecognitionrealtime-b1c32.appspot.com"
})






#importing Mode Images
folderPath="Images"
imgpathList=os.listdir(folderPath)

#imgespathList=['1.png','2.png', '3.png', '4.png']
imgsList=[]
studentIds=[]
for path in imgpathList:
	imgsList.append(cv2.imread(os.path.join(folderPath, path)))
	studentIds.append(os.path.splitext(path)[0])
	fileName=os.path.join(folderPath, path)
	bucket=storage.bucket()
	blob=bucket.blob(fileName)
	blob.upload_from_filename(fileName)
	



#print(studentIds)


def findEncodings(imagesList):
	encodeList=[]
	for img in imagesList:
		img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		encode=face_recognition.face_encodings(img)[0]
		encodeList.append(encode)
	return encodeList
	


print("Encodings Started ......")
encodeListKnown=findEncodings(imgsList)
encodeListKnownWithIds=[encodeListKnown, studentIds]
#print(encodeListKnown)
print("Encodings Complete")	



file=open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()

print("File Saved....")

