import cv2
import numpy as np
from time import sleep
import math
import argparse
import time
from tracking import *

class TwoPointLine:
    def __init__(self, cv_line):
        self.x1, self.y1, self.x2, self.y2 = cv_line

    def reverse(self):
        self.x1, self.y1, self.x2, self.y2 = self.x2, self.y2, self.x1, self.y1


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @staticmethod
    def from_line(line):
        return Vector((line.x2 - line.x1), (line.y2 - line.y1))

    def dot(self, other_vec):
        return self.x * other_vec.x + self.y * other_vec.y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def angle(self, other_vec):
        if abs(self.dot(other_vec)/(self.norm()*other_vec.norm())) > 1:
            return 0
        return math.acos(self.dot(other_vec)/(self.norm()*other_vec.norm())) * 180 / math.pi

    def add_vector(self, other_vec):
        return Vector((self.x + other_vec.x), (self.y + other_vec.y))


class Final(ITrackingCore):
    def __inital_filter(self,line):
        minimal_dy = 40
        maximal_dx = 20
        if abs(line.x2 - line.x1) < maximal_dx and abs(line.y2 - line.y1) > minimal_dy:
            return True
        return False

    def __sub_score_core(self, x):
        return 1/(x**6 + 1)

    def __sub_score(self, value, centre, error_allowed):
        return self.__sub_score_core((value - centre) / error_allowed * 0.5)

    def __secondary_filter(self,line1,line2,yellow_frame):
        if line1.y2 < line1.y1:
            line1.reverse()
        if line2.y2 < line2.y1:
            line2.reverse()
        vec_L = Vector.from_line(line1)
        vec_R = Vector.from_line(line2)
        # to check the color between the two lines are yellow
        left,right = min(line1.x1,line1.x2,line2.x1,line2.x2),max(line1.x1,line1.x2,line2.x1,line2.x2)
        up,down = min(line1.y1,line2.y1,line1.y2,line2.y2),max(line1.y1,line2.y1,line1.y2,line2.y2)
        if up != down and left!=right:
            if not yellow_frame[left:right, up:down] is None:
                mean = np.mean(yellow_frame[left:right, up:down])
        else:
            mean = 0
        total_score = 1
        total_score *= self.__sub_score(vec_L.angle(vec_R), 0, 10)
        total_score *= self.__sub_score(vec_L.angle(Vector(1,0)),90,10)
        total_score *= self.__sub_score(abs(line1.x1 - line2.x1),3,10)
        total_score *= self.__sub_score(abs(line1.y1 - line2.y2),3,10)
        total_score *= self.__sub_score(mean,127,50)
        return total_score

    def find(self, frame):
        origin = img = cv2.resize(frame,(640,360),0)
        b,g,r = cv2.split(img)
        yellow_frame = cv2.addWeighted(g,0.5,(255-b),0.5,0)
        ret,yellow_frame = cv2.threshold(yellow_frame,100,255,cv2.THRESH_BINARY)
        # yellow_frame = cv2.addWeighted(cv2.addWeighted(g,0.333,b,0.333,0),0.666,r,0.333,0)
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        _,_,v = cv2.split(hsv)
        blurred = cv2.GaussianBlur(v,(3,31),0)
        bw = 255 - np.array(blurred)
        bw = bw // 60 * 255
        edges = cv2.Canny(bw, 100, 300, apertureSize=5)
        # edges = cv2.dilate(edges, np.ones((3, 3), np.uint8))
        minLineLength, maxLineGap = 20, 5
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 20, None, minLineLength, maxLineGap)
        for l in lines:
            l1 = TwoPointLine(l[0])
            cv2.line(origin,(l1.x1,l1.y1),(l1.x2,l1.y2), (0, 255, 0), 1)
        vertical_lines = []
        scores= {}
        for line in lines:
            line1 = TwoPointLine(line[0])
            if self.__inital_filter(line1):
                vertical_lines.append(line1)
        for line1 in vertical_lines:
            for line2 in vertical_lines:
                scores[self.__secondary_filter(line1,line2,yellow_frame)] = (line1,line2)
        keylist = list(scores.keys())
        x,y = 0,0
        if len(keylist) > 0:
            keylist.sort()
            final_line,_ = scores[keylist[-1]]
            cv2.line(origin, (final_line.x1, final_line.y1), (final_line.x2, final_line.y2), (0, 0, 255), 3)
            # print((final_line.x1, final_line.y1), (final_line.x2, final_line.y2))
            print(keylist[-1])
            x = int((final_line.x1 - final_line.x2) / 2)
            y = int((final_line.y1 - final_line.y2) / 2)
        # return ((final_line.x1+final_line.x2)/2, (final_line.y1+final_line.y2)/2, 3, [origin, edges,yellow_frame])
        return (x,y,0,[origin, edges,yellow_frame])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
                    help="path to the (optional) video file")
    ap.add_argument("-c", "--camera",
                    help="index of camera")
    ap.add_argument("-o","--output",
                    help="path to save the video")
    args = vars(ap.parse_args())
    if args.get("video", False):
        vs = args.get("video", False)
    elif args.get("camera", False):
        vs = int(args.get("camera", False))
    else:
        vs = 0

    cv = CVManager(vs,                  # choose the first web camera as the source
                   enable_imshow=True,  # enable image show windows
                   delay=5,outputfolder=args.get("output"))
    cv.add_core("Flare", Final(), True)
    cv.start()
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        print("Stopping remaining threads...")
        cv.stop()

if __name__ == '__main__':
    main()
