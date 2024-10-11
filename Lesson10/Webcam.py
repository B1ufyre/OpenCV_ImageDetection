import cv2
Webcam = cv2.VideoCapture(0)
eye_detector = cv2.CascadeClassifier("haarcascade_eye.xml")
while True:
    ret, img = Webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eye = eye_detector.detectMultiScale(gray, 500, 4)
    print(eye)
    for (x,y,w,h) in eye:
        cv2.rectangle(img, (x,y), (x+w, y+h), (240, 65, 3), 5)
    cv2.imshow("Video", img)
    k = cv2.waitKey(10)
    if k == 27:
        break