import cv2

image = cv2.imread("Image/redFrame.png", cv2.IMREAD_ANYCOLOR)
cv2.imshow("RedFrame", image)
cv2.waitKey(0)
cv2.destroyAllWindows()