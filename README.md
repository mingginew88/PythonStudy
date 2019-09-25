# PythonStudy


1. Project Setting
OS : MacOS
version : python 3.7.0 
Tool : VSCode

2. Python Environment Variable
# Mac homebrew Install
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# insert command line in terminal
sudo vi .profile
# 키보드에서 i키를 입력(insert)
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
# esc를 누른 후에
:wq
# Python3 Install
brew install python3
# Python Version Check
python3 --version
# OpenCV Install
brew tap brewsci/science
brew install opencv
# 설치경로로 이동 후
/usr/local/opt/opencv/lib/python3.7/site-packages/cv2/python-3.7
# 파일 복사(cv2.cpython-37m-darwin.so)
cp ./cv2.cpython-36m-darwin.so ./cv2.so
# python3 경로에 추가
echo /usr/local/opt/opencv/lib/python3.7/site-packages >> /usr/local/lib/python3.7/site-packages/opencv3.pth
# brew link
brew link --overwrite python3




# 다시 정리하기.
# 소스 점검하기.
