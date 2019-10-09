import cv2

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

# cv2.blur(원본 이미지, (커널 x크기, 커널 y크기), 앵커 포인트, 픽셀 외삽법)
# 커널크기 - 이미지에 흐림 효과를 적용할 크기 설정
# 앵커 포인트 - 커널에서의 중심점을 의미 (-1,-1) 사용시 자동적으로 커널의 중심점으로 할당
# 픽셀 외삽법?????? 이해가안간다.
dst = cv2.blur(src, (9,9), anchor=(-1,-1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()