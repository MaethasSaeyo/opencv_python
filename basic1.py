import cv2

cap = cv2.VideoCapture(0)

while (True):
    chack , frame = cap.read()#รับภาพจากกล้องframe : frame
    cv2.imshow("Output",frame)

    if cv2.waitKey(1) & 0xff == ord("e"):#กดeเพื่อปิดกล้อง
        break


cap.release()#เครียแรม
cv2.destroyAllWindows()


