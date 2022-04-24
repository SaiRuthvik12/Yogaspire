import mediapipe as mp
import cv2 as cv
import time

class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon = 0.5, trackCon =0.5):
        
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)

    
    def findPose(self, img, draw = True):

        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        
        if self.results.pose_landmarks:
            if draw:
                 self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img

    def findPosition(self,img,draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                #print(id,lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id,cx,cy])
                if draw:
                    cv.circle(img, (cx,cy),5,(0,0,255),cv.FILLED)

        return lmList



def main():
    cap = cv.VideoCapture(0)
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img,False)
        if(len(lmList)!=0):
            print(lmList[14])
            cv.circle(img, (lmList[14][1],lmList[14][2]),15,(0,0,255),cv.FILLED)
        cv.imshow("Image",img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()