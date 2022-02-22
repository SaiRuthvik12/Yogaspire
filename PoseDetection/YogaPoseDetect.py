import cv2 as cv
import posemodule as pm

cap = cv.VideoCapture(0)
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img,False)
    if(len(lmList)!=0):
        #print(lmList[14])
        if(lmList[15][1]-lmList[16][1]<50):
            print("CLAPPED")
        #cv.circle(img, (lmList[14][1],lmList[14][2]),15,(0,0,255),cv.FILLED)
    cv.imshow("Image",img)
    cv.waitKey(1)