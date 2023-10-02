import cv2
img = cv2.imread("D:/2023/opencv/cv_1/opencv_python/image/cat.jpg")
imgresize = cv2.resize(img,(400,400))

#วาดสี่เหลี่ยม
#rectangle(ภาพ,มุมที่1(บนซ้าย),มุมที่2(ล่างขวา),สี(BGR),ความหนา)
cv2.rectangle(imgresize,(0,0),(100,200),(0,0,255),1)


cv2.imshow("Outpen",imgresize)#แสดงผลภาพ
cv2.waitKey(0)#delay
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows