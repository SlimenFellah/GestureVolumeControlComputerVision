import cv2
import time
import mediapipe
import numpy
import numpy as np

import handTrackModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()
#volume.SetMasterVolumeLevel(-64.0, None)
minVol = volumeRange[0]
maxVol = volumeRange[1]


cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4,480)
detector = htm.handDetector(detConf = 0.8)
pTime = 0
#vol = volume.GetMasterVolumeLevel()
#print(vol)
#height = np.interp(vol,[-64,0],[150,400])
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lm_list = detector.findPosition(img, draw=False)
    if len(lm_list) != 0:
        #print(lm_list[4],  lm_list[8])
        x1,y1 = lm_list[4][1],lm_list[4][2]
        x2,y2 = lm_list[8][1], lm_list[8][2]
        cx,cy = (x1+x2)//2 , (y1+y2)//2

        cv2.circle(img,(x1,y1),15,(150,0,150),cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (150, 0, 150), cv2.FILLED)
        cv2.circle(img, (cx, cy), 15, (150, 0, 150), cv2.FILLED)
        cv2.line(img,(x1,y1),(x2,y2),(150,0,150),3)
        length = math.hypot(x2-x1,y2-y1)
        if(length < 50):
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
        #vol range -64 0
        #length range 50 350
        # 50 150 -> 85 400 (0,255,0)
        height = 400 - ((int(length) / 300) * 250)
        height = max(height,150)
        cv2.rectangle(img,(85,400),(50,150),(0,255,0),3)
        cv2.rectangle(img,(85,400),(50,int(height)),(0,255,0),cv2.FILLED)
        vol = np.interp(length,[50,350],[minVol,maxVol])
        volPer = np.interp(length,[50,350],[0,100])
        cv2.putText(img,f'{int(volPer)}%', (50,140),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),1)
        volume.SetMasterVolumeLevel(vol, None)
        print(int(length), vol)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    fps = int(fps)
    pTime=cTime
    #  cv2.rectangle(img, (85, 400), (50,150), (0, 255, 0), 3)
    #  cv2.rectangle(img,(85,400),(50,int(height)),(0,255,0),cv2.FILLED)
    cv2.putText(img,f'fps : {fps}',(40,50), cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),1)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
