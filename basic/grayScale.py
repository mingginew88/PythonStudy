import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# cv2.cvtColor(원본이미지, 색상 변환 코드)
# 이미지의 색상공간을 변경
dst = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

cv2.imshow("src", src)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()