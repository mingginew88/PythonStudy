import numpy as np
import cv2

# 기하학적 변환 - 영상이나 이미지를 펼치거나 좁힐 수 있음
# WarpPerspective의 경우 4개의 점을 매핑 (4개의 점을 이용한 변환)
# WarpAffine의 경우 3개의 점을 매핑 (3개의 점을 이용한 변환)

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)
height, width, channel = src.shape

# 좌표의 순서는 좌상, 우상, 우하, 좌하 순서입니다. numpy 형태로 선언
# dtype을 float32 형식으로 선언해야 사용가능
# srcPoint : 원본 이미지에서 4점 변환
srcPoint=np.array([[300, 200], [400, 200], [500, 500], [200, 500]], dtype=np.float32)
# dstPoint : 결과 이미지의 위치
dstPoint=np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)
# cv2.getPerspectiveTransform(원본 좌표 순서, 결과 좌표 순서)
matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)
# cv2.warpPerspective(원본 이미지, 매트릭스, (결과 이미지 너비, 결과 이미지 높이))를 사용하여 이미지를 변환할 수 있습니다.
dst = cv2.warpPerspective(src, matrix, (width, height))

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()