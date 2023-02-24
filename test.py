import cv2
vid = cv2.VideoCapture(0)
vid1 = cv2.VideoCapture(1)
while(True):
    ret, frame = vid.read()
    ret1, frame1 = vid1.read()
    cv2.imshow('frame1', frame)
    cv2.imshow('frame2', frame1)   
    print("nnn")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
vid1.release()
cv2.destroyAllWindows()