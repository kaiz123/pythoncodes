import cv2
import sys
print(sys.argv)
#cascPath = sys.argv[1]

faceCascade = cv2.CascadeClassifier('C:\Users\user\Desktop\opencv/build\etc\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\Users\user\Desktop\opencv/build\etc\haarcascades\haarcascade_eye.xml')
smilePath = "C:\Users\user\Desktop\opencv/build\etc\haarcascades/haarcascade_smile.xml"
smileCascade = cv2.CascadeClassifier(smilePath)



video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        #flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        flags=cv2.CASCADE_SCALE_IMAGE

        

    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        smile = smileCascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # for (x, y, w, h) in smile:
        #     print "Found", len(smile), "smiles!"
        #     cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # cv2.imshow('Smile Detector', frame)
    # c = cv2.waitKey(7) % 0x100
    # if c == 27:
    #     break


# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()