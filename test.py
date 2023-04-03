import numpy as np
import cv2

#初始化数据
imgName = '18.jpg'  #待处理图像
#待处理的目标坐标，一行四个元素，分别是目标中心点的x、y坐标，目标宽、高
img = cv2.imread(imgName,1)

'''cv2.imshow('image', img)
cv2.waitKey(0)'''

# 用128进行灰度涂抹

img_o=img.copy()
img = cv2.bitwise_xor(img, img_o)
ls,num,r = [], 0, 1024

for i in open("03.txt"):
    num = num + 1
    arr = i.split('\t')
    print(arr)
    #print(type(arr))
    ls.append(arr)
    xmin = int((float(arr[0]) * r) - (float(arr[2]) * r) / 2)
    xmax = int((float(arr[0]) * r) + (float(arr[2]) * r) / 2)
    ymin = int((float(arr[1]) * r) - (float(arr[3]) * r) / 2)
    ymax = int((float(arr[1]) * r) + (float(arr[3]) * r) / 2)
    cv2.rectangle(img, ((xmin), (ymin)), ((xmax), (ymax)), (256, 256, 256), -1)
    cv2.putText(img, str(num), ((xmin + 15, ymin + 15)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
cv2.imwrite('output.jpg', img)
cv2.imshow("image",img)
cv2.waitKey(0)
cnt = int(input("请输入你想要进行保护的区域序号:"))
#print(ls[cnt-1])
x1 = int((float(ls[cnt-1][0]) * r) - (float(ls[cnt-1][2]) * r) / 2)
x2 = int((float(ls[cnt-1][0]) * r) + (float(ls[cnt-1][2]) * r) / 2)
y1 = int((float(ls[cnt-1][1]) * r) - (float(ls[cnt-1][3]) * r) / 2)
y2 = int((float(ls[cnt-1][1]) * r) + (float(ls[cnt-1][3]) * r) / 2)
cv2.rectangle(img, ((x1), (y1)), ((x2), (y2)), (128, 128, 128), -1)
cv2.imshow("img_oprate",img)
cv2.waitKey(0)
cv2.imwrite("result.jpg",img)