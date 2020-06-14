import cv2
import numpy as np
import math
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
delayTime = 1
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

#Announce fire Cascade-classifier
hand_cascade = cv2.CascadeClassifier('hand_haar_cascade.xml')
#Initialize and start realtime video capture
cap = cv2.VideoCapture(0)
while (True):
    #get image from webcam
    ret, img = cap.read()

    #Blur images and convert images to grayscale 
    blur = cv2.GaussianBlur(img,(5,5),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    #define value threshold
    retval2,thresh1 = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    #Call to function detectMultiScale
    hand = hand_cascade.detectMultiScale(thresh1, 1.3, 5)
    mask = np.zeros(thresh1.shape, dtype = "uint8")

    #Loop for Create framework use Detect Hand
    for (x,y,w,h) in hand:
        cv2.rectangle(img,(x,y),(x+w,y+h), (122,122,0), 2)
        cv2.rectangle(mask, (x,y),(x+w,y+h),255,-1)

    #Find Contours for Detect Hand
    img2 = cv2.bitwise_and(thresh1, mask)
    final = cv2.GaussianBlur(img2,(7,7),0)
    contours, hierarchy = cv2.findContours(final, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    cv2.drawContours(final, contours, -1, (0, 255, 0), 2)
    if len(contours) > 0:
        cnt=contours[0]
        hull = cv2.convexHull(cnt, returnPoints=False)
        # finding convexity defects
        defects = cv2.convexityDefects(cnt, hull)
        count_defects = 0
        strl1 = " "
        strl2 = " "

        if defects is not None:
            for i in range(defects.shape[0]):
                p,q,r,s = defects[i,0]
                start = tuple(cnt[p][0])
                end = tuple(cnt[q][0])
                far = tuple(cnt[r][0])
                # find length of all sides of triangle
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                # apply cosine rule here
                angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57.29
                # ignore angles > 90 and highlight rest with red dots
                if angle <= 90:
                    count_defects += 1

        #Show text from find Contours
        if count_defects == 1:
            strl1 = "On_Lamp1"
            cv2.putText(img,"On_Lamp1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 2:
            strl2 = "On_Lamp2"
            cv2.putText(img, "On_Lamp2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 3:
            strl1 = "Off_Lamp1"
            cv2.putText(img,"Off_Lamp1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 4:
            strl2 = "Off_Lamp2"
            cv2.putText(img,"Off_Lamp2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)


        #Control Relay with Contours 
        if(strl1=="On_Lamp1"):
            GPIO.output(16, True) # NO is now connected through
            #time.sleep(delayTime)
        elif (strl1=="Off_Lamp1"):
            GPIO.output(16, False) # NC is now connected through
            #time.sleep(delayTime)
        if(strl2=="On_Lamp2"):
            GPIO.output(20, True) # NO is now connected through
            #time.sleep(delayTime)
        elif (strl2=="Off_Lamp2"):
            GPIO.output(20, False) # NC is now connected through
            #time.sleep(delayTime)

        
    cv2.imshow('img1',img)
    if(cv2.waitKey(1) & 0xFF== ord('q')):
        break
GPIO.cleanup()
cv2.destroyAllWindows()



