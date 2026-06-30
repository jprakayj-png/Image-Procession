import cv2 as cv 

img = cv.imread("Black-White-cmdn.png")

h = img.shape[0]  # height
w = img.shape[1] # width
center = (w // 2 , h // 2) # find position of center of picture

M = cv.getRotationMatrix2D(center , 27 , 1.0) 
rotate = cv.warpAffine(img , M , (w,h)) 

cv.imshow("rotate" , rotate)
cv.waitKey(0)
cv.destroyAllWindows()