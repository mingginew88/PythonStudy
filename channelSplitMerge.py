import cv2
import numpy as np

#  OpenCV의 가산혼합의 삼원색 기본 배열순서는 BGR

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(src)
# cv2.merge((채널1, 채널2, 채널3))
# 순서가 변경될 경우, 원본 이미지와 다른 색상으로 표현
inversebgr = cv2.merge((r, g, b))

# 이미지[높이, 너비, 채널]을 이용하여 특정 영역의 특정 채널만 불러옴
# [:, :, n]을 입력할 경우, 이미지 높이와 너비를 그대로 반환하고 n번째 채널만 반환
b = src[:,:,0]
g = src[:,:,1]
r = src[:,:,2]

# 검은색 빈 공간 이미지가 필요할 때는
# np.zeros((높이, 너비, 채널), dtype=정밀도)을 이용하여 빈 이미지를 생성
height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype = np.uint8)
bgz = cv2.merge((b, g, zero))

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", inversebgr)
cv2.imshow("bgz", bgz)
cv2.waitKey(0)
cv2.destroyAllWindows()