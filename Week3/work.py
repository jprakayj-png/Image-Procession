import cv2 as cv 
import datetime

vdo = cv.VideoCapture(0) # 0 is for webcam

while(vdo.isOpened()) :
    ret , frame = vdo.read()
    if (ret == True) :

        # make a circle at the center of the frame
        center = (frame.shape[1] // 2 , frame.shape[0] // 2)
        cv.circle(frame,center,50,(0,255,0),3)
    
        # make a rectnagle over the border around the frame
        cv.rectangle(frame,(0,0),(frame.shape[1],frame.shape[0]),(255,191,0),20)

        # make a line diagonal line
        cv.line(frame,(0,0),(frame.shape[1],frame.shape[0]),(0,0,255),5)
        
        # point the time on the edge 
        now_time = datetime.datetime.now().strftime("%H:%M:%S") # get time 
        cv.putText(frame, f"Live Video : {now_time}" , (15,40) , 4 , 1 , (0,0,0) , 2)
        
        cv.imshow("Frame" , frame) #show frame
        
        key = cv.waitKey(33) 
        
        if (key == ord('q')) : # exit to end video showing
            break
    
    else : # if the video can't show
        print("Can't show vdo")
        break

vdo.release() #start showing video
cv.destroyAllWindows()