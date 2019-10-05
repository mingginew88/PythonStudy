import cv2

# HSV(Hue, Saturation, Value)
# Hue(색상) - 색의 질 (0~180 값)
# Saturation(채도) - 색의 선명도 (0~255 값)
# Value(명도) - 색의 밝기 (0~255 값)

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)
# bgr -> hsv 로 채널 변경
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# 각 속성 분할 하기위해 split 사용하여 채널 분리
h, s, v = cv2.split(hsv)

cv2.imshow("h", h)

# hue 범위 조정하여 특정 색상만 출력
# cv2.inRange(단일 채널 이미지, 최솟값, 최댓값)
# 주황색 약 8~20 범위
h = cv2.inRange(h, 8, 20)
# 해당 마스크를 이미지 위에 덧씌워 해당 부분만 출력
orange = cv2.bitwise_and(hsv, hsv, mask=h)
# hsv -> bgr로 변경
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)
cv2.imshow("orange", orange)

cv2.imshow("s", s)
cv2.imshow("v", v)

cv2.waitKey(0)
cv2.destroyAllWindows()