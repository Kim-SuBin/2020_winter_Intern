import qrcode
import cv2 as cv
addr = 'https://github.com/Kim-SuBin/2020_winter_Intern/blob/master/Project/parkingLotQR/B4.png?raw=true' # url
#원하는 url 넣기

img = qrcode.make(addr)

img.save('B4qrcode.png') #원하는 사진 이름을 입력하면 qr코드 생성
# 저장

cv.waitKey(0)
cv.destroyAllWindows()
