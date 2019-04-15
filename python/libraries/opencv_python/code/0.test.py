import cv2 as cv
print(cv.__version__) # 导入成功
src = cv.imread("C:\opencv\demo.jpg") # 载入图片
cv.namedWindow("image", cv.WINDOW_AUTOSIZE) # 创建窗口并设置其为动态大小
cv.imshow("image",src) # 显示图片
cv.waitKey(0)
cv.destroyallWindows()
