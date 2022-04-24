from re import L
import cv2 as cv
import posemodule as pm
import math

wCam,hCam = 1920,1080
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = pm.poseDetector()

def findAngle(img, lmList, p1, p2, p3, draw=False):
    x1,y1 = lmList[p1][1:]
    x2,y2 = lmList[p2][1:]
    x3,y3 = lmList[p3][1:]

    angle = math.degrees(math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2,x1-x2))
    if(angle<0):
        angle = 360+angle
    #print(angle)
    if(angle>180):
        angle = 360-angle

    if draw:
        cv.circle(img, (x1,y1),15,(0,0,255),cv.FILLED)
        cv.circle(img, (x2,y2),15,(0,0,255),cv.FILLED)
        cv.circle(img, (x3,y3),15,(0,0,255),cv.FILLED)

    return angle

def pose1(img,lmList):

    if findAngle(img,lmList,11,13,15)>150 and findAngle(img,lmList,12,14,16)>150:
        if findAngle(img,lmList,23,11,13)>160 and findAngle(img,lmList,24,12,14)>160:
            cv.putText(img, "POSE DETECTED - MOUNTAIN",(50,50),cv.FONT_HERSHEY_PLAIN,4,(255,0,255),10)

def pose2(img,lmList):
    if findAngle(img,lmList,12,14,16)>160 and findAngle(img,lmList,11,13,15)>160:
        if findAngle(img,lmList,23,11,13)>70 and findAngle(img,lmList,24,12,14)>70 and findAngle(img,lmList,23,11,13)<110 and findAngle(img,lmList,24,12,14)<110 :

            if findAngle(img, lmList,12,24,26)>65 and findAngle(img,lmList,11,23,25)>100 and findAngle(img, lmList,12,24,26)<110 and findAngle(img,lmList,11,23,25)<130:
        #    if findAngle(img, lmList,23,25,27)>160 and findAngle(img, lmList,24,26,28)>75:
                cv.putText(img, "POSE DETECTED - WARRIOR 2",(50,50),cv.FONT_HERSHEY_PLAIN,4,(255,0,255),10)  

def pose3(img,lmList):
    if findAngle(img,lmList,12,14,16)>70 and findAngle(img,lmList,11,13,15)>70 and findAngle(img,lmList,12,14,16)<100 and findAngle(img,lmList,11,13,15)<100:
        if findAngle(img, lmList,12,24,26)>65 and findAngle(img,lmList,11,23,25)>65 and findAngle(img, lmList,12,24,26)<100 and findAngle(img,lmList,11,23,25)<100:
            cv.putText(img, "POSE DETECTED - GODDESS",(50,50),cv.FONT_HERSHEY_PLAIN,4,(255,0,255),10)




while True:
    success, img = cap.read()
    img = cv.flip(img,1)
    #img = cv.resize(img, (1280,720))
    img = detector.findPose(img)
    lmList = detector.findPosition(img,False)
    if len(lmList)!=0 :

        pose1(img,lmList)
        pose2(img,lmList)
        pose3(img,lmList)
        #if findAngle(img,lmList,11,13,15)>90 and findAngle(img,lmList,12,14,16)>90:
        #    cv.putText(img, "Pose Detected",(50,50),cv.FONT_HERSHEY_PLAIN,4,(255,0,255),10)
        #if(lmList[15][1]-lmList[16][1]<50):
        #    print("CLAPPED")
        #cv.circle(img, (lmList[14][1],lmList[14][2]),15,(0,0,255),cv.FILLED)
        
    cv.imshow("Image",img)
    cv.waitKey(1)