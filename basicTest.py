import cv2
import numpy as np

# opencv version check
print(cv2.__version__)

# Receive video from built-in camera or an external camera
# VideoCapture(n) n means a device number of the camera
# if you want to connect a camera additionally, change the device number of the camera
capture = cv2.VideoCapture(0)

# setting frame width and height
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Repeat video output
while True:
    # using capture.read(),  Get the camera status and frame
    # ret saves the state of the camera and returns True if it is operating normally. If it doesn't work, it returns False.
    ret, frame = capture.read()
    # Floats an image in a window
    cv2.imshow("VideoFrame", frame)
    # Repeat while statement until key input
    # if you want to use specific key, Use the following sentence : ord('specific key')
    if cv2.waitKey(1) > 0: break

# Release memory 
capture.release()
# Close all windows
# if you want to close specific window, input the title in method.
cv2.destroyAllWindows()