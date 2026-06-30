import cv2 as cv 

img = cv.imread("Black-White-cmdn.png")

resize_img = cv.resize(img , None ,fx = 2.0 , fy = 0.5) # None means we're aren't giving the exact scale output

cv.imshow("resize" , resize_img)
cv.waitKey(0)
cv.destroyAllWindows()