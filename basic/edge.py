import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 가장자리 검출??? 종류 3가지의 차이를 모르겠네...
# cv2.Canny(원본 이미지, 임계값1, 임계값2, 커널 크기, L2그라디언트)를 이용하여 가장자리 검출을 적용
canny = cv2.Canny(src, 100, 255)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

cv2.imshow("canny", canny)
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()