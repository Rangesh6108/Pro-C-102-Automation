import cv2
import time
import random

starttime = time.time()

def takeSnapshot():
    randomName = random.randint(0,10000000000)
    videoCaptureobj = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureobj.read()
        imgname = "img" + str(randomName) + ".png"
        cv2.imwrite(imgname, frame)
        starttime = time.time
        result=False
    return imgname
    print("Your photo has been taken!")
    videoCaptureobj.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time() - starttime) >= 6):
            takeSnapshot()

main()