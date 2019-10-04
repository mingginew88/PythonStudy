import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# 이미지 색상 반전
# 연산 종류 : not, and, or, xor
#dst = cv2.bitwise_not(src)
#dst = cv2.bitwise_and(src)
#dst = cv2.bitwise_or(src)
dst = cv2.bitwise_xor(src)

cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()