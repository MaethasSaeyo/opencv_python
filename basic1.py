import cv2
img = cv2.imread("D:/2023/opencv/cv_1/opencv_python/image/cat.jpg")
imgresize = cv2.resize(img,(400,400))

#วาดเส้นตรง
#line(ภาพ,จุดเริ่มต้น(x,y),จุดสุดท้าย(x,y),สี(BGR),ความหนา)
cv2.arrowedLine(imgresize,(0,200),(150,200),(0,0,255),5)

cv2.imshow("Outpen",imgresize)#แสดงผลภาพ
cv2.waitKey(0)#delay
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows