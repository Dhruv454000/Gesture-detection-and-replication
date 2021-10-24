from keras.models import load_model
import matplotlib.pyplot as plt
model=load_model('D:\deep learning\handrecognition_model.h5')
import numpy as np
from keras_preprocessing import image
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

cam = cv2.VideoCapture(0)
segmentor=SelfiSegmentation()
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    frame=segmentor.removeBG(frame,(0,0,0),threshold=0.4)
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test",frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
test=cv2.imread('opencv_frame_0.png',cv2.IMREAD_GRAYSCALE) 
test=cv2.resize(test,(320,120))
plt.grid(False)
print(test.shape)
cv2.imshow('sample',test)
cv2.waitKey(0)
test=image.img_to_array(test)
test=np.expand_dims(test,axis=0)
result=model.predict(test)
r=np.argmax(result)
print(r)