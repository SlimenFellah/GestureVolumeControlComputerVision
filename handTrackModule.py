import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self,mode = False,max_hands=2,complexity=1,detConf = 0.5,trackConf =0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detConf = detConf
        self.trackConf = trackConf
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.max_hands,self.complexity,self.detConf,self.trackConf)
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self, img,draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for result in self.results.multi_hand_landmarks:
                if draw :
                    self.mpDraw.draw_landmarks(img, result, self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,nHand = 0,draw = True):
        lm_list = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[nHand]
            for id, lm in enumerate(myHand.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                lm_list.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lm_list


def main():
    pTime = 0
    cap = cv2.VideoCapture(1)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lm_list = detector.findPosition(img,0)
        if len(lm_list) != 0 :
            print(lm_list[4])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        fps = int(fps)
        pTime = cTime
        cv2.putText(img, f'FPS : {str(fps)}', (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ =="__main__":
    main()