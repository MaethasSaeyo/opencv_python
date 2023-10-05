import cv2

img = cv2.imread("image/boy.jpg")

#อ่านไฟล์สำหรับ classifficaation
face_cascade = cv2.CascadeClassifier("Detect/haarcascades_haarcascade_frontalface_default.xml")

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#จำแนกใบหน้า
scaleFactor = 1.1
minNeighber = 3
face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

#แสดงตำแหน่งที่เจอในหน้า
for (x,y,w,h) in face_detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)


cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()