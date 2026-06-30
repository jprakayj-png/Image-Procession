import cv2 as cv 

img = cv.imread("Week1/Naval_Ensign_of_Thailand.png")

for i in range (img.shape[0]) :
    for j in range (img.shape[1]) :
        b = img[i,j,0] 
        g = img[i,j,1]
        r = img[i,j,2]
        grey = 0.114 * b + 0.587 * g + 0.299 * r 
        if (grey >= 128) :
            img[i,j] = [255,255,255] # black
        else :
            img[i,j] = [0,0,0] # white

cv.imshow("Greyscale_Picture" , img)
cv.waitKey(0)
cv.destroyAllWindows()