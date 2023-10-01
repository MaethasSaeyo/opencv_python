import cv2
img = cv2.imread("D:/2023/opencv/cv_1/opencv_python/image/cat.jpg")

cv2.imshow("Outpen",img)#แสดงผลภาพ
cv2.waitKey(delay=0)
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows
