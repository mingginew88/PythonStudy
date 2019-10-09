import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# image info (the value of height, width, channel)
height, width, channel = src.shape

# getRotationMatrix2D(node X, node Y, rotation angle, image magnification)
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()