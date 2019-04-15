import numpy as np
import cv2 as cv
image = cv.imread("/home/luo/Videos/1.jpg")
rows, cols = image.shape[0:2]
horiz, vert = 160, 90
r1,c1,r2,c2=[0,0,0,0]
k = 1
while r2<=rows:
    r1,r2 = [r2,r2 + horiz]
    while c2<=cols:
        c1, c2 = [c2,c2 + vert]
        img = image[r1:r2, c1:c2]
        cv.imwrite(str(k)+".jpg",img)
        k += 1

