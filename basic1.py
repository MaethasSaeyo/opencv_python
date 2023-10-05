#Mouse Event
import cv2
import numpy as np
img = cv2.imread("image/cat.jpg")
imgresize = cv2.resize(img,(700,700))
def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = imgresize[y,x,0]
        green = imgresize[y,x,1]
        red = imgresize[y,x,2]
        imgcolor = np.zeros([300,300,3],np.uint8)
        imgcolor[:] = [blue,green,red]
        cv2.imshow("Result",imgcolor)



cv2.imshow("Output",imgresize)#แสดงผลภาพ

#ทำงานกับmouse
cv2.setMouseCallback("Output",click)


cv2.waitKey(delay=0)
cv2.destroyAllWindows()#คืนทรัพร์ยากรให้windows