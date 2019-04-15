import numpy as np

import cv2


if __name__ == '__main__':

    sz1 = 200

    sz2 = 400

    print('generate an image matrix(%d*%d)' % (sz1,sz2))

    img = np.zeros((sz1,sz2,3),np.uint8)

    pos1 = np.random.randint(200,size=(2000,1))

    pos2 = np.random.randint(400,size=(2000,1))

    #set the pixel value at random point

    for i in range(2000):
        

        img[pos1[i],pos2[i],[0]]=np.random.randint(0,255)

        img[pos1[i],pos2[i],[1]]=np.random.randint(0,255)

        img[pos1[i],pos2[i],[2]]=np.random.randint(0,255)

    cv2.imshow('preview',img)

    cv2.waitKey()

    cv2.destroyAllWindows()