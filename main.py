import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector

vid_capture = cv.VideoCapture(0)
vid_capture.set(3,1280)
vid_capture.set(4,720)

handDetector = HandDetector(detectionCon=0.8, maxHands=2)

while True:

    success, img = vid_capture.read()
    hands, img = handDetector.findHands(img)

    cv.imshow("Image", img)
    cv.waitKey(1) #TODO: create a command to stop the video feed