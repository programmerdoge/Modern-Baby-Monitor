import cv2
import sys 

print(cv2.__version__)
dispW=1280
dispH=960
flip=2 
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=200, height=246, format=NV12, framerate=10/2 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
cascPath = "/home/jetson/Desktop/PyPro/openCV/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

while True:
    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

    for(x,y,w,h) in faces: 
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,225,0),2)
        cv2.imshow('nanoCam',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
