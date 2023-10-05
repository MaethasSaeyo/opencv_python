#Mouse Event
import cv2
import numpy as np
img =np.zeros([400,500,3])

points = []

def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,0,255),4)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-2],points[-1],(255,0,80),5)


        cv2.imshow("Output",img)
        



cv2.imshow("Output",img)#แสดงผลภาพ

#ทำงานกับmouse
cv2.setMouseCallback("Output",click)


cv2.waitKey(delay=0)
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows