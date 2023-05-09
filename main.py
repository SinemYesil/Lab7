import cv2
import numpy as np

img=cv2.imread('He_Man_and_The_Masters_of_Universe-_1983.jpg') #q1

cv2.imshow('He_Man', img)
cv2.waitKey(0)
cv2.destroyAllWindows()#q2
blue = img[:, :, 0]

cv2.imshow('blue', img)
cv2.waitKey(0)
cv2.destroyAllWindows()#q3

b, g, r=cv2.split(img)
b=img[:, :, 0]
g=img[:, :, 1]
r=img[:, :, 2]

cv2.imshow('b', b)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('g', g)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('r', r)
cv2.waitKey(0)
cv2.destroyAllWindows()#q4

b,g,r= cv2.split(img)
cv2.imshow('b', b)
cv2.waitKey(0)

cv2.imshow('g', g)
cv2.waitKey(0)

cv2.imshow('r', r)
cv2.waitKey(0)

cv2.destroyAllWindows()#q5

g=np.zeros_like(g)
img_rb=cv2.merge((b, g, r))

cv2.imshow('q6',img_rb)

cv2.waitKey(0)
cv2.destroyAllWindows()#q6

height, width, channels=img.shape
for i in range (height):
    for j in range(width):
        g[i,j]=0
img_rb=cv2.merge((b, g,r))

cv2.imshow("Final",img_rb)
cv2.waitKey(0)

cv2.destroyAllWindows()#q7