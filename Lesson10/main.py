import cv2
car_video = cv2.VideoCapture("video1.avi")
car_detector = cv2.CascadeClassifier("cars.xml")
while True:
    ret, img = car_video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    car = car_detector.detectMultiScale(gray, 1.1, 2)
    print(car)
    for (x,y,w,h) in car:
        cv2.rectangle(img, (x,y), (x+w, y+h), (240, 65, 3), 5)
        cv2.imshow("Video", img)
    k = cv2.waitKey(10)
    if k == 27:
        break