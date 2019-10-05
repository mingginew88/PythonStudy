import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# dst = src 로 이용한다면, 이미지 원본에 영향을 미칠 수 있기 때문에 복제하여 사용한다.
dst = src.copy()
# [height,width]
#dst = src[100:600,200:700]
# 잘라낼 영역 설정
roi = src[100:600,200:700]
# dst 범위에 해당 이미지 붙여넣기
dst[0:500,0:500] = roi
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()