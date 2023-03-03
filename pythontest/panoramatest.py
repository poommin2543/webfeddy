# import cv2
# import numpy as np
# import glob
# img1 = cv2.imread('C:/Users/Mr.Noom/Documents/webfeddy/imgtest/hippo11.jpg')
# img2 = cv2.imread('C:/Users/Mr.Noom/Documents/webfeddy/imgtest/hippo22.jpg')
# img1 = cv2.resize(img1,[640,460],interpolation = cv2.INTER_AREA)
# img2 = cv2.resize(img2,[640,460],interpolation = cv2.INTER_AREA).
# cv2.imshow("img1",img1)
# cv2.imshow("img2",img2)

# imageStitcher = cv2.Stitcher_create()
# error,stitcher_img = imageStitcher.stitch([img1,img2])
# # if not error:
# cv2.imshow("img3",stitcher_img)
# # print(stitcher_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2
# image_paths=['C:/Users/Mr.Noom/Documents/webfeddy/imgtest/cam1.png','C:/Users/Mr.Noom/Documents/webfeddy/imgtest/cam2.png','C:/Users/Mr.Noom/Documents/webfeddy/imgtest/cam3.png','C:/Users/Mr.Noom/Documents/webfeddy/imgtest/cam4.png']
# # initialized a list of images
# imgs = []
# for i in range(len(image_paths)):
#     imgs.append(cv2.imread(image_paths[i]))
#     imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
#     # this is optional if your input images isn't too large
#     # you don't need to scale down the image
#     # in my case the input images are of dimensions 3000x1200
#     # and due to this the resultant image won't fit the screen
#     # scaling down the images 
# # showing the original pictures
# cv2.imshow('1',imgs[0])
# cv2.imshow('2',imgs[1])
# # cv2.imshow('3',imgs[2])
  
# stitchy=cv2.Stitcher.create()
# (dummy,output)=stitchy.stitch(imgs)
  
# if dummy != cv2.STITCHER_OK:
#   # checking if the stitching procedure is successful
#   # .stitch() function returns a true value if stitching is 
#   # done successfully
#     print("stitching ain't successful")
# else: 
#     print('Your Panorama is ready!!!')
  
# # final output
# # cv2.imshow('final result',output)
# print(output)
  
# cv2.waitKey(0)


import cv2
vid = cv2.VideoCapture(0)
vid1 = cv2.VideoCapture(1)
while(True):
    ret, frame = vid.read()
    ret1, frame1 = vid1.read()
    cv2.imshow('frame1', frame)
    cv2.imshow('frame2', frame1)
    try:
        imageStitcher = cv2.Stitcher_create()
        error,stitcher_img = imageStitcher.stitch([frame,frame1])
        cv2.imshow('frame3', stitcher_img)
    except:
        print("error")
        continue
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
vid1.release()
cv2.destroyAllWindows()
