import cv2

cap = cv2.VideoCapture(0)
fourcss = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("output.avi",fourcss,20.00,(640,480))

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    
    if check == True:#checkว่าวีดีโอยังเล่นอยู่รึเปล่า
       
        cv2.imshow("Output",frame)
        result.write(frame)
        if cv2.waitKey(1) & 0xff == ord("e"):#กดeเพื่อปิดvideo
            break
    
result.release()
cap.release()#เครียแรม
cv2.destroyAllWindows()


