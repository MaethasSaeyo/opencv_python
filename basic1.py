import cv2
img = cv2.imread("D:/2023/opencv/cv_1/opencv_python/image/cat.jpg")
imgresize = cv2.resize(img,(400,400))

#วาดข้อความ
#putText(ภาพ,ข้อความ,พิกัดที่จะใส่ข้อความ(x,y),font,ขนาดข้อความ,สี,ความหนา)
cv2.putText(imgresize,"Hello World",(100,200),3,1,(0,0,255),2)


cv2.imshow("Outpen",imgresize)#แสดงผลภาพ
cv2.waitKey(0)#delay
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows