import cv2

# 영상이나 이미지의 색상을 검출 할 때, cv2.inRange()의 영역이 한정되어 색상을 설정하는 부분이 한정

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 빨강 영역은 0~5, 170~180 범위
# cv2.inRange(다채널 이미지, (채널1 최솟값, 채널2 최솟값, 채널3 최솟값), (채널1 최댓값, 채널2 최댓값, 채널3 최댓값))
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
# cv2.addWeighted(이미지1, 이미지1 비율, 이미지2, 이미지2 비율, 가중치)
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

red = cv2.bitwise_and(hsv, hsv, mask = added_red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

cv2.imshow("red", red)
cv2.waitKey(0)
cv2.destroyAllWindows()