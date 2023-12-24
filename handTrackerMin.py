import cv2
import mediapipe as mp
import time



cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for result in results.multi_hand_landmarks:
            for id,lm in enumerate(result.landmark):
                #print(id,lm)
                h,w,c = img.shape
                cx,cy = int(lm.x * w), int(lm.y * h)
                print(id,cx,cy)
                if id ==4 :
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            mpDraw.draw_landmarks(img, result, mpHands.HAND_CONNECTIONS)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    fps = int(fps)
    cv2.putText(img,f'FPS : {str(fps)}', (10,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow("Image",img)
    pTime = cTime
    cv2.waitKey(1)