import cv2
import mediapipe as mp
import time
import handTrackModule as htm
pTime = 0
cap = cv2.VideoCapture(1)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img,draw=False)
    lm_list = detector.findPosition(img,draw=False)
    if len(lm_list) != 0 :
        print(lm_list[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    fps = int(fps)
    pTime = cTime
    cv2.putText(img, f'FPS : {str(fps)}', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
