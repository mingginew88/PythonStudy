import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# 이진화 적용을 위해 grayscale로 변환
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# ret, dst를 이용하여 이진화 결과 저장 ret에는 임계값 저장
# cv2.threshold(그레이스케일 이미지, 임계값, 최댓값, 임계값 종류)
# 임계값은 이미지의 흑백을 나눌 기준값을 의미
# 100 이하인 경우에는 0  100 이상인 경우에는 최댓값으로 변경
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

