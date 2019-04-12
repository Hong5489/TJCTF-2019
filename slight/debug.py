import cv2
import numpy as np 
from math import sqrt
from pwn import *
from PIL import Image
image = Image.open('test.jpg')
img = cv2.imread('test.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,
                            param1=43,param2=15,minRadius=25,maxRadius=63)
coordinates = []
distance = []
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    print i[2]
    coordinates.append([float(i[0]/3),float(i[1]/3)])

for i in range(len(coordinates)):
    coordCopy = coordinates[:]
    del coordCopy[i]
    for c in coordCopy:
        distance.append(np.longdouble(sqrt((coordinates[i][0]-c[0])**2 + (coordinates[i][1]-c[1])**2)))


print min(distance)
cimg = cv2.resize(cimg, (image.width-600, image.height-600))
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
