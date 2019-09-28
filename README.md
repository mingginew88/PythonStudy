# Python study

## Project Setting

> - OS : MacOS
> - version : python 3.7.0
> - Tool : vscode

## Python Environment Variable
## Mac homebrew Install
```terminal
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
## insert command line in terminal

```terminal
$ sudo vi .profile
$ export PATH=/usr/local/bin:/usr/local/sbin:$PATH 
# 패스 등록
....
$ brew install python3 # brew를 통해 파이선3 설치
```


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
