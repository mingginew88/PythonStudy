import cv2
import datetime

capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# fourcc : 디지털 미디어 포맷 코덱 (인코딩 방식 선택)
# FourCC 종류 : CVID, Default, DIB, DIVX, H261, H263, H264, IV32, IV41, IV50, IYUB, MJPG, MP42, MP43, MPG4, MSVC, PIM1, Prompt, XVID
# 단일 채널 이미지의 경우, 사용할 수 없는 디지털 미디어 포맷 코드가 존재
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True :
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)) :
        capture.open("/Users/dean/Room/Study/Python/PythonStudy/video/nar.mp4")
    ret, frame = capture.read()

    cv2.imshow("VideoFrame", frame)
    # 현재시각 (날짜_시간-분-초)
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    # 키보드 키 값 저장 (33ms)
    key = cv2.waitKey(33)
    
    if key == 27 : # esc key
        break
    elif key == 49 : # number 1 key
        print("캡쳐")
        cv2.imwrite("/Users/dean/Room/Study/Python/PythonStudy/capture/"+str(now)+".png", frame)
    elif key == 32 :  # space bar key
        print("녹화 시작")
        record = True
        # cv2.VideoWriter("경로 및 제목", 비디오 포맷 코드, FPS, (녹화 파일 너비, 녹화 파일 높이))
        # FPS(Frame Per Second) : 영상이 바뀌는 속도를 의미
        # frame.shape는 (높이, 너비, 채널)의 값이 저장
        video = cv2.VideoWriter("/Users/dean/Room/Study/Python/PythonStudy/capture/"+str(now)+".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 13 :  # enter key
        print("녹화 중지")
        record = False
        video.release()
    
    if record == True :
        print("녹화 중...")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()
