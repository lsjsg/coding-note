import cv2
import numpy as np
from time import sleep
import math
# from tracking import ITrackingCore

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

class Final:
    def __init__(self,img):
        self.img = img
        b,g,_ = cv2.split(img)
        self.yellow_frame = np.array(g) - np.array(b)

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

    def __secondary_filter(self,line1,line2):
        if line1.y2 < line1.y1:
            line1.reverse()
        if line2.y2 < line2.y1:
            line2.reverse()
        vec_L = Vector.from_line(line1)
        vec_R = Vector.from_line(line2)
        # to check the color between the two lines are yello
        left,right = min(line1.x1,line2.x2),max(line1.x1,line2.x2)
        up,down = min(line1.y1,line2.y2),max(line1.y1,line2.y2)
        mean = np.mean(self.yellow_frame[left:right, up:down])
        total_score = 1
        total_score *= self.__sub_score(vec_L.angle(vec_R), 0, 10)
        total_score *= self.__sub_score(abs(line1.x1 - line2.x1),3,10)
        total_score *= self.__sub_score(mean,160,50)
        return total_score

    def filtering(self):
        origin = img = cv2.resize(self.img,(640,360),0)
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        _,_,v = cv2.split(hsv)
        blurred = cv2.GaussianBlur(v,(3,31),0)
        bw = 255 - np.array(blurred)
        bw = bw // 60 * 255
        edges = cv2.Canny(bw, 100, 300, apertureSize=5)
        # edges = cv2.dilate(edges, np.ones((3, 3), np.uint8))
        minLineLength, maxLineGap = 50, 150
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 20, None, minLineLength, maxLineGap)
        vertical_lines = []
        scores= {}
        for line in lines:
            line1 = TwoPointLine(line[0])
            if self.__inital_filter(line1):
                vertical_lines.append(line1)
        for line1 in vertical_lines:
            for line2 in vertical_lines:
                scores[self.__secondary_filter(line1,line2)] = (line1,line2)
        keylist = list(scores.keys())
        keylist.sort()
        final_line1,final_line2 = scores[keylist[-1]]
        final_line = TwoPointLine((
            int((final_line1.x1 + final_line2.x1)/2),
            int((final_line1.x2 + final_line2.x2)/2),
            int((final_line1.y1 + final_line2.y1)/2),
            int((final_line1.y2 + final_line2.y2)/2) ))

        cv2.line(edges, (final_line.x1, final_line.y1), (final_line.x2, final_line.y2), (0, 255, 0), 3)
        return origin, edges

if __name__ == "__main__":
    for i in range(6,12):
        directory = "/home/luo/Pictures/"+str(i)+".png"
        img = cv2.imread(directory)
        t = Final(img)
        origin, edges = t.filtering()
        cv2.imshow("orign",origin)
        cv2.imshow("edges",edges)
        cv2.waitKey(0)
        sleep(3)
        cv2.destroyAllWindows()