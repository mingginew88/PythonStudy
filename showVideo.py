import cv2

capture = cv2.VideoCapture("video/nar.mp4")

while True :

    # Compare the current frame count with the total frame count
    # CAP_PROP_POS_FRAMES : current frame count
    # CAP_PROP_FRAME_COUNT : total frame count
    # if current frame and total frame count is the same, it means the final frame.
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("video/nar.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    # play the frame per 33ms 
    if cv2.waitKey(33) > 0 : break

capture.release()
cv2.destroyAllWindows()