import cv2
import numpy as np

# 输入图片
imgName = '0327_01.jpg'

img = cv2.imread(imgName,1)
cv2.imshow('img',img)
cv2.waitKey(0)

r=1024

#the keep region
xmin1=int((0.089844*r)-(0.144531*r)/2)
xmax1=int((0.089844*r)+(0.144531*r)/2)
ymin1=int((0.486328*r)-(0.408203*r)/2)
ymax1=int((0.486328*r)+(0.408203*r)/2)

#the remove region
xmin2=int((0.812012*r)-(0.375977*r)/2)
xmax2=int((0.812012*r)+(0.375977*r)/2)
ymin2=int((0.317871*r)-(0.407227*r)/2)
ymax2=int((0.317871*r)+(0.407227*r)/2)

#show the origin img
cv2.rectangle(img,((xmin1),(ymin1)),((xmax1),(ymax1)),(0,0,0),-1)
cv2.rectangle(img,((xmin2),(ymin2)),((xmax2),(ymax2)),(256,256,256),-1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.imwrite('05.png',img)

#make mask
mask = np.zeros(img.shape[:2], dtype=np.uint8)
cv2.rectangle(mask,(0,0),(1024,1024),(128,128,128),-1)
cv2.rectangle(mask,((xmin1),(ymin1)),((xmax1),(ymax1)),(0,0,0),-1)
cv2.rectangle(mask,((xmin2),(ymin2)),((xmax2),(ymax2)),(256,256,256),-1)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('06.png',mask)
