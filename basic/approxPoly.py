import cv2

# 영상이나 이미지에서 윤곽선의 근사 다각형을 검출

src = cv2.imread("Image/narImage.jpeg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
binary = cv2.bitwise_not(binary)

contours, hierachy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

# 색인값과 하위 윤곽선 정보 반복
for contour in contours:
    # 근사치 정확도 계산을 위해 윤ㄷ곽선 전체 길이의 2% 활용
    # cv2.arcLength(윤곽선, 폐곡선)
    # 윤곽선 : 검출된 윤곽선들이 저장된 Numpy 배열
    # 폐곡선 : 검출된 윤곽선이 닫혀있는지, 열려있는지 설정
    # 폐곡선이 True 인 경우, 윤곽선이 닫혀 최종 길이가 더 길어짐.
    epsilon = cv2.arcLength(contour, True) * 0.02
    # cv2.approxPolyDP(윤곽선, 근사치 정확도, 폐곡선)
    # 근사치 정확도 : 입력된 다각형(윤곽선)과 반환될 근사화된 다각형 사이의 최대 편차 간격
    # 근사치 정확도는 값이 낮을 수록 원본 윤곽과 유사
    approx_poly = cv2.approxPolyDP(contour, epsilon, True)

    # 근사 다각형 반복하여 근사점 이미지 위에 표시
    for approx in approx_poly:
        cv2.circle(src, tuple(approx[0]), 3, (255, 0, 0), -1)

# 다각형 근사는 더글라스-패커(Douglas-Peucker) 알고리즘을 사용

cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
