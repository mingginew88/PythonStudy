import cv2
import datetime

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True :
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == 27 : # esc
        break
    elif key == 49 : # 1
        print("캡쳐")
        cv2.imwrite("/Users/dean/Room/Study/Python/PythonStudy/capture/"+str(now)+".png", frame)
    elif key == 32 : # space bar
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("/Users/dean/Room/Study/Python/PythonStudy/capture/"+str(now)+".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 13 : # enter
        print("녹화 중지")
        record = False
        video.release()
        
    if record == True:
        print("녹화 중...")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()