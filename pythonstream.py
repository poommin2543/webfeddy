import cv2
print(cv2.getBuildInformation())
cap = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1")
# cap = cv2.VideoCapture(0)

# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=10.168.1.177 port=50001", cv2.CAP_GSTREAMER, 0, 25.0, (1920,1080))
# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=103.82.249.178 port=8005", cv2.CAP_GSTREAMER, 0, 25.0, (960,360))
# out = cv2.VideoWriter('appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=1500 ! rtph264pay ! udpsink host=103.82.249.178 port=8005',cv2.CAP_GSTREAMER,0, 25, (640,480), True)
# out = cv2.VideoWriter("appsrc ! video/x-raw, format=BGR ! queue ! videoconvert ! video/x-raw, format=BGRx ! nvvidconv ! omxh264enc ! video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! udpsink host=10.168.1.177 port=50001", cv2.CAP_GSTREAMER, 0, 25.0, (1920,1080))
# gst_str_rtp = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink host=103.82.249.178 port=8004"
# out = cv2.VideoWriter(gst_str_rtp, 0, 30, (640, 480), True)
gst_str_rtp = "appsrc ! video/x-raw,format=BGR ! queue ! videoconvert ! video/x-raw,format=BGRx ! nvvidconv !\
     video/x-raw(memory:NVMM),format=NV12,width=640,height=360,framerate=52/1 ! nvv4l2h264enc insert-sps-pps=1  \
        insert-vui=1 idrinterval=30bitrate=1000000 EnableTwopassCBR=1  ! h264parse ! rtph264pay ! udpsink host=103.82.249.178 port=8005 auto-multicast=0"
    

out = cv2.VideoWriter(gst_str_rtp, cv2.CAP_GSTREAMER, 0, float(52), (640, 480), True)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        try:
            out.write(frame)
            # print("Writing")
            # print(out)
        except Exception:
            print("Error writing")
        # cv2.imshow('img1',frame)
        # print('writing frame')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    


# Release everything if job is finished
cap.release()
out.release()