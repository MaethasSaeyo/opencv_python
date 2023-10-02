#Mouse Event
import cv2
img = cv2.imread("output.jpg")

def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y)
        cv2.putText(img,text,(x,y),1,1,(0,0,255,),2)
        cv2.imshow("Output",img)



cv2.imshow("Output",img)#แสดงผลภาพ

#ทำงานกับmouse
cv2.setMouseCallback("Output",click)


cv2.waitKey(delay=0)
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows