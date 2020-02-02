import cv2
import sys 

print(cv2.__version__)
dispW=500
dispH=500
flip=2 
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=200, height=246, format=NV12, framerate=1/2 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)
cascPath = "/home/jetson/Desktop/PyPro/openCV/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
numberFound=0

while True:
    ret, frame = cam.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

    for(x,y,w,h) in faces: 
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,225,0),2)
        cv2.imshow('nanoCam',frame)
        
    faceFound =(len(faces))
    # for faceFound in faceFound:
    if faceFound == 0:
        numberFound+=1
        print("No face" , +numberFound)
    else:
        print("baby is here") 
        numberFound=0
    if numberFound >=15:
        users_ref.update({
        'Baby': 'Check the baby'
    
        })
        numberFound =0
        # break
    
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()