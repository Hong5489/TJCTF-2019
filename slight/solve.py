import cv2
import numpy as np 
from math import sqrt
from pwn import *
from PIL import Image
s = remote('p1.tjctf.org',8005)
j = 0
while(1):
    try:
        print s.recvuntil("Find the minimum distance between the centers of two circles to continue:\n")
        text = s.recvuntil("\n>>>")[:-4].decode('base64')
        open('test.jpg','w').write(text)
        image = Image.open('test.jpg')
        image = image.resize((image.width*3,image.height*3),Image.ANTIALIAS)
        image.save('test.jpg')
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
            #print i[0]-150,i[1]-150
            coordinates.append([float(i[0]/3),float(i[1]/3)])

        for i in range(len(coordinates)):
            coordCopy = coordinates[:]
            del coordCopy[i]
            for c in coordCopy:
                distance.append(np.longdouble(sqrt((coordinates[i][0]-c[0])**2 + (coordinates[i][1]-c[1])**2)))

        s.sendline(str(min(distance)))
    # s.interactive()
        print min(distance),j
        j += 1
    except:
        # print s.recv()
        # cimg = cv2.resize(cimg, (image.width-150, image.height-150))
        # cv2.imshow('detected circles',cimg)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # break
        j = 0
        print s.recv()
        s.close()
        s = remote('p1.tjctf.org',8005)
