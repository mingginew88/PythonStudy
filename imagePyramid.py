import cv2


# Changing the size of the image and sampling to the desired level

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

height, width, channel = src.shape
dst = cv2.pyrUp(src, dstsize=(width*2, height*2), borderType=cv2.BORDER_DEFAULT)
dst2 = cv2.pyrDown(src)

# dst2 - 1/8 size of the src
for i in range(0,2) :
    dst2 = cv2.pyrDown(dst2)

cv2.imshow("src", src)
#cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()