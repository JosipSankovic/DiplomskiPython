import cv2 as cv
import numpy as np
import os
import sys

# skripta za uzimanje 3 frame-a iz videa i spremanje u folder kao sliku od 640x640
count=0

def showVideo(dir,name):
    global count
    frameCount=0
    

    cap = cv.VideoCapture(dir+'/'+name)

    
    fps=cap.get(cv.CAP_PROP_FPS)
    totalFrames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    dirForSavingImages=sys.argv[2]

    picturesToTake=3
    picturesTaken=0

    print(dir)
    print(name)
    print(".....q")

    while cap.isOpened():
        cap.set(cv.CAP_PROP_POS_FRAMES, int(((picturesTaken+1)*totalFrames)/picturesToTake))
        ret, frame = cap.read()
        if not ret:
            break
        
        if picturesTaken==picturesToTake:
            break
        
        frame=cv.resize(frame,(640,640),interpolation=cv.INTER_AREA)
        cv.imwrite(dirForSavingImages+"/slika"+str(count)+".jpg",frame)
        count=count+1
        picturesTaken=picturesTaken+1
        
        
    
        
    cap.release()
    cv.destroyAllWindows()



if __name__=="__main__":

    
    dirName=sys.argv[1]
    with os.scandir(dirName) as entries:
        videoSkip=0
        videoSkipCount=0
        for entry in entries:
            videoSkipCount=videoSkipCount+1
            if videoSkip-videoSkipCount<0:
                showVideo(dirName,entry.name)
    


