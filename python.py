# import cv2
# import numpy as np 
# import os
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"
# vcap = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1", cv2.CAP_FFMPEG)
# vcap1 = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1", cv2.CAP_FFMPEG)
# while(1):
#     ret, frame = vcap.read()
#     ret1, frame1 = vcap1.read()
#     if ret == False:
#         print("Frame is empty")
#         break
#     else:
#         cv2.imshow('VIDEO', frame)
#         cv2.imshow('VIDEO1', frame1)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# vcap.release()

# vcap1.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

# import cv2

# frame0 = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1", cv2.CAP_FFMPEG)
# frame1 = cv2.VideoCapture(0)
# while 1:

#    ret0, img0 = frame0.read()
#    ret1, img00 = frame1.read()
#    img1 = cv2.resize(img0,(360,240))
#    img2 = cv2.resize(img00,(360,240))
#    if (frame0):
#        cv2.imshow('img1',img1)
#        cv2.imshow('img2',img2)
# #    if (frame1):
      

#    k = cv2.waitKey(30) & 0xff
#    if k == 27:
#       break

# frame0.release()
# # Releasing the video capture object.
# # frame1.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np

frame_width = 960
frame_height = 360
flip = 0

gst_str_rtp = "appsrc ! video/x-raw, format=I420 ! queue ! videoconvert ! \
      width=960,height=360,framerate=52/1 ! nvvidconv ! omxh264enc ! \
          video/x-h264, stream-format=byte-stream ! h264parse ! rtph264pay pt=96 config-interval=1 ! \
        udpsink host=34.143.225.243 port=8004"

# Create two video capture objects, one for the RTSP stream and one for the local webcam. 
frame0 = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1", cv2.CAP_FFMPEG)
# frame1 = cv2.VideoCapture("rtsp://lordtopzz01:Siripong01@192.168.50.59:554/stream1", cv2.CAP_FFMPEG)
# frame1 = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'H264')
out = cv2.VideoWriter(gst_str_rtp, fourcc, 52, (frame_width, frame_height), True)
while 1:

   # Read from both video capture objects and store the frames in img0 and img00 respectively. 
   ret0, img0 = frame0.read()
   # ret1, img1 = frame1.read()

   # Resize both frames to 360x240 and store them in img1 and img2 respectively. 
   img1 = cv2.resize(img0,(360,240))
   # img2 = cv2.resize(img1,(360,240))

   # Display both frames in separate windows named 'img1' and 'img2'. 
   if (frame0):
       images_1_2_h = np.hstack((img1, img1))
       images = np.hstack((images_1_2_h, images_1_2_h))
       cv2.imshow('img1',images)
       out.write(images)
      #  cv2.imshow('img2',img2)

   # Wait for user input (ESC key). If ESC is pressed, break out of the loop and close all windows/release objects before exiting program execution. 
   k = cv2.waitKey(30) & 0xff
   if k == 27:
      break

    # Release the video capture object associated with frame 0 before closing all windows/exiting program execution    
frame0.release()      
cv2.destroyAllWindows()
  