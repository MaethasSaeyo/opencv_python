import cv2
import datetime as dt
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:#checkว่าวีดีโอยังเล่นอยู่รึเปล่า
        currenDate = str(dt.datetime.now())
        cv2.putText(frame,currenDate,(10,30),1,1,(0,0,0),1)
        cv2.imshow("Output",frame)
        
        if cv2.waitKey(1) & 0xff == ord("e"):#กดeเพื่อปิดvideo
            break
    else:
        break
cap.release()#เครียแรม
cv2.destroyAllWindows()