import cv2

# cap = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.58:554/stream1")
cap = cv2.VideoCapture(0)

# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=10.168.1.177 port=50001", cv2.CAP_GSTREAMER, 0, 25.0, (1920,1080))
# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=34.143.225.243 port=8004", cv2.CAP_GSTREAMER, 0, 25.0, (960,360))
out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=1500 ! rtph264pay ! udpsink host=34.143.225.243 port=8004',cv2.CAP_GSTREAMER,0, 25, (640,480), True)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        try:
            out.write(frame)
            # print("Writing")
            # print(out)
        except Exception:
            print("Error writing")
        cv2.imshow('img1',frame)
        # print('writing frame')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    


# Release everything if job is finished
cap.release()
out.release()