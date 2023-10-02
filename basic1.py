import cv2
img = cv2.imread("D:/2023/opencv/cv_1/opencv_python/image/cat.jpg")
imgresize = cv2.resize(img,(400,400))

#วาดวงกลม
#circle(ภาพ,ตำแหน่งจุดศูนย์กลาง(x,y),รัศมี,สี(BGR),ความหนา)
cv2.circle(imgresize,(250,190),100,(0,0,255),5)


cv2.imshow("Outpen",imgresize)#แสดงผลภาพ
cv2.waitKey(0)#delay
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows