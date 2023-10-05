#Mouse Event
import cv2
img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img,(700,700))
def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = imgresize[y,x,0]
        green = imgresize[y,x,1]
        red = imgresize[y,x,2]
        text = "BGR = "+str(blue)+","+str(green)+","+str(red)
        cv2.putText(imgresize,text,(x,y),1,1,(0,0,255,),2)
        cv2.imshow("Output",imgresize)



cv2.imshow("Output",imgresize)#แสดงผลภาพ

#ทำงานกับmouse
cv2.setMouseCallback("Output",click)


cv2.waitKey(delay=0)
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows