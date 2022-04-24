import mediapipe as mp
import cv2 as cv
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv.VideoCapture(0)
while True:
  success, img = cap.read()
  imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
  results = pose.process(imgRGB)
  if results.pose_landmarks:
    mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

  cv.imshow("Image",img)
  cv.waitKey(1)