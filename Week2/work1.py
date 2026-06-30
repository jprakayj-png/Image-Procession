import cv2 as cv 
import numpy as np ;

# read image 
img = cv.imread("Black-White-cmdn.png")

# getting width , height
width = img.shape[1]
height = img.shape[0]

tx ,ty = -90 , 100 # position picture to move
M = np.float32([[1,0,tx] , [0,1,ty]]) # transform matrix
move = cv.warpAffine(img , M , (width , height)) # picture move , img.shape[1] = width , img.shape[0] = height
cv.imshow("Move" , move)
cv.waitKey(0)
cv.destroyAllWindows()