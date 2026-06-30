import cv2 as cv 

#1 read picture (cv.imread)

flg = cv.imread('Week1/Naval_Ensign_of_Thailand.png' , 1) 

''' in cv.IMREAD_COLOR (1)  : shows picture with color
can change cv.IMREAD_COLOR (1) ---> cv.IMREAD_GRAYSCALE (0)  : Show picture in Grayscale
can change cv.IMREAD_COLOR (1) ---> cv.IMREAD_UNCHANGED (-1) : Show picture in default '''

#2 display picture (cv.imshow)

if (flg is None) :
    print("Couldn't find / read picture")
else :
    cv.imshow("Thailand Royal Navy Ensign" , flg) 
    cv.waitKey(0) # wait for the picture to show , if not have this line the picture would quickly show that eye can't catch in time
    cv.destroyAllWindows() # clear picture

# ---------------------

cmdn = cv.imread('Week1\\Flag_for_Commander-in-Chief_of_the_Royal_Thai_Navy.png' , 0)

resize = cv.resize(cmdn,(300,300)) # resize the picture to 300 x 300

#3 save file_pic (cv.imwrite) to vscode

cv.imwrite('Black-White-cmdn.png' , cmdn)  