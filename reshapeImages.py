import cv2
import os
path="./Images/"

imagesPath=os.listdir(path)
pathToSave="./ImagesResized"
if os.path.exists(pathToSave):
	pass
else:
	os.makedirs(pathToSave)
for image in imagesPath:
	img=cv2.imread(os.path.join(path,image))
	img=cv2.resize(img,(216,216))
	id=os.path.splitext(image)[0]
	cv2.imwrite(f"{pathToSave}/{id}.png",img)

