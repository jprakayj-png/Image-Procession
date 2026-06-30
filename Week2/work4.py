import numpy as np
import cv2 as cv

img = cv.imread("Black-White-cmdn.png")

width = img.shape[1]
height = img.shape[0]

# Part 1 moving 100 pixels in right direction
tx = 100 
M = np.float32([[1,0,tx] , [0,1,0]])
move = cv.warpAffine(img , M ,(width,height))

# Part 2 rotating the picture 92 degrees and make scale picture double
center = (width // 2 , height // 2)
R = cv.getRotationMatrix2D(center , 92 , 2.0)
rotate = cv.warpAffine(move,R,(width,height))

cv.imshow("rotate" , rotate)
cv.waitKey(0)
cv.destroyAllWindows()