import cv2


src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# flip(Original image, Symmetry method)
# symmetry method -> 0 : Upside down, 1 : Invert left and right
#dst = cv2.flip(src, 0)
dst = cv2.flip(src, 1)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()