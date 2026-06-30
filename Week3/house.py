import numpy as np 
import cv2 as cv 

img = np.full((1024,1024,3) , 255 , np.uint8)

# making cloud
np.random.seed()
for _ in range(1000):
    x = np.random.randint(-200, 1200)
    y = np.random.randint(-100, 1024)
    length = np.random.randint(15, 50)
    gray =np.random.randint(20,255)
    cv.circle(img , (x ,y) , length, (gray,gray,gray) , -1)

# body of the house , mountain , river 
cv.ellipse(img , (512+100 , 512+200) , (450,200) , 0 , 180 , 360 , (34,139,34)  , -1)
cv.ellipse(img , (512-100 , 512+200) , (425,200) , 0 , 180 , 360 , (34,139,34)  , -1)
cv.ellipse(img , (512+100 , 512+135) , (450,200) , 0 , 180 , 360 , (34,139,34)  , -1)
cv.rectangle(img , (512,512) , (512+320 , 512-200) , (255,51,255) , -1)
cv.rectangle (img , (515,310) , (650,400) , (255,229,204) , -1)
cv.rectangle (img , (700,310) , (830,400) , (255,229,204) , -1)
cv.line(img,(520,355) , (650 , 355) , 5)
cv.line(img,(700,355) , (830 , 355) , 5)
cv.line(img , (585,310) , (585,400), 5)
cv.line(img , (765,310) , (765,400), 5)
cv.rectangle (img , (0,700) , (1023,1023) , (255,51,51) , -1)
cv.rectangle(img , ( 550,450) , (600,512) ,(0,76,153) , -1)
cv.rectangle(img , ( 750,450) , (800,512) ,(0,76,153) , -1)
cv.circle(img , (590,490) , 7 , (0,255,255) , -1)
cv.circle(img , (790,490) , 7 , (0,255,255) , -1)

# roof
cv.fillPoly(img , [np.array([[512,312] , [512+320,312] , [672,162]] , dtype= np.int32)] , (255,51,153))
cv.ellipse(img , (672,240) ,(40,30) , 90, 0 , 360 , (255,229,204) , -1)
cv.line(img , (672,200) , (672,280) , 5)
cv.line(img , (640,240) , (702,240) , 5)

# making rain
for i in range(1500):
    x = np.random.randint(-200, 1200)
    y = np.random.randint(-100, 1024)
    length = np.random.randint(15, 50)
    cv.line(img, (x, y), (x - int(length * 0.4), y + length), (180, 180, 180), 1)

# showing picture
cv.imshow("Farmhouse" , img)
cv.waitKey(0)
cv.destroyAllWindows()
