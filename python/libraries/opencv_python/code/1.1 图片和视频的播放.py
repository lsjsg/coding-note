# 加载与显示图像
import cv2 as cv

def get_image_info(image): # 获取图片大小及形状信息
    print(image.shape)
    print(image.size)
    print(image.dtype)

def video_demo():
    capture = cv.VideoCapture(0) # 打开电脑相机,获取信息
    while (True):
        ret, frame = capture.read() # 获取视频的返回值以及帧信息
        cv.imshow("video",frame)
        c = cv.waitKey(50) # 此项为每一帧加载的延时, 若设置的延时小于实际延时, 则以实际延时为准, 若设置延时高于实际延时, 则每一帧间隔时间增加为所设置的延时
        if c ==27:  # 当点击时间为ESC时, 则可以关闭视频播放窗口
            cv.destroyAllWindows()
            break

def save_image():
    img = cv.imread("D:\opencv\demo.jpg",0)
    cv.imshow("image",img)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()
    elif k == ord("s"):
        cv.imwrite("D:/opencv/test.jpg",img)
        cv.destroyAllWindows()

src = cv.imread("D:\opencv\demo.jpg") # 载入图片
cv.namedWindow("image", cv.WINDOW_AUTOSIZE) # 创建窗口并设置其为动态大小
cv.imshow("image",src) # 显示图片

get_image_info(src)
save_image()
# video_demo()

cv.waitKey(0)
cv.destroyallWindows()