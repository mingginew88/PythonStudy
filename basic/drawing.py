import cv2
import numpy as np

# np.unit8 동작하지않음.
#src = np.zeros((768,1366,3),dtype=np.unit8)
src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# cv2.line(이미지, (x1, y1), (x2, y2), (B, G, R), 두께, 선형 타입)
cv2.line(src, (100,100), (1200,100), (0,0,255), 3, cv2.LINE_AA)
# cv2.circle(이미지, (x, y), 반지름, (B, G, R), 두께, 선형 타입)
cv2.circle(src, (300,350), 50, (0,255,0), cv2.FILLED, cv2.LINE_4)
# cv2.rectangle(이미지, (x1, y1), (x2, y2), (B, G, R), 두께, 선형 타입)
cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)
# cv2.ellipse(이미지, (x, y), (lr, sr), 각도, 시작 각도, 종료 각도, (B, G, R), 두께, 선형 타입)
cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

# 선형 타입은 설정하지 않아도 사용가능

# poly 함수를 사용하는 경우, numpy 형태로 저장된 위치 좌표가 필요
pts1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])
# cv2.polylines(이미지, [위치 좌표], 닫힘 유/무, (B, G, R), 두께, 선형 타입 )
cv2.polylines(src, [pts1], True, (0, 255, 255), 2)
# cv2.fillPoly(이미지, [위치 좌표], (B, G, R), 두께, 선형 타입 )을 이용하여 내부가 채워진 다각형 그리기
cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)
# cv2.putText(이미지, 문자, (x, y), 글꼴, 글자 크기, (B, G, R), 두께, 선형 타입)로 문자 그리기
cv2.putText(src, "CHARACTER", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

# cv2.FILLED : 내부채우기
# cv2.LINE_4 : 4점 이웃 연결
# cv2.LINE_8 : 8점 이웃 연결
# cv2.LINE_AA : AntiAlias

cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()