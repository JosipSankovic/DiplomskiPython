from ultralytics import YOLO
import supervision as sv
import cv2 as cv
import os

# program za trazenje objekata na slici i stvaranje datoteka s koordinatima za treniranje pomoću
# prijašnje istreniranih verzija yolov8 modela

model=YOLO("best.pt")



def detectAndWrite(detections,imgName,dir):
    f=open(dir+"/"+imgName+".txt","w")
    for data in detections.xyxy:
        #x
        x=((data[0]+data[2])/2)/640
        #y
        y=((data[1]+data[3])/2)/640
        #width
        width=data[2]/640-data[0]/640
        #height
        height=data[3]/640-data[1]/640
        

       
        f.write('0 '+f'{x:.5f}'+' '+f'{y:.5f}'+' '+f'{width:.5f}'+' '+f'{height:.5f}'+'\n')
    f.close()




dirName='E:/datasetLjeto/images'

with os.scandir(dirName) as entries:

    for entry in entries:
        results=model(dirName+'/'+entry.name)[0]
        detection=sv.Detections.from_yolov8(results)
        detectAndWrite(detections=detection,imgName=entry.name,dir='E:\datasetLjeto'+'/labels')
            