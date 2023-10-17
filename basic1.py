import cv2


#อ่านไฟล์สำหรับ classifficaation
face_cascade = cv2.CascadeClassifier("Detect/haarcascades_haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture("image/Video (1).mp4")



while (cap.isOpened()):
    check, frame = cap.read()
    if check == True :
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #จำแนกใบหน้า
        face_detect = face_cascade.detectMultiScale(gray_img,1.1,4)

        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)

        cv2.imshow("Output",frame)

        if cv2.waitKey(1) & 0xff == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()