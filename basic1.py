import cv2

cap = cv2.VideoCapture("D:/2023/opencv/cv_1/opencv_python/image/Video (1).mp4")

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:#checkว่าวีดีโอยังเล่นอยู่รึเปล่า
        cv2.imshow("Output",frame)

        if cv2.waitKey(1) & 0xff == ord("e"):#กดeเพื่อปิดvideo
            break
    else:
        break

cap.release()#เครียแรม
cv2.destroyAllWindows()


