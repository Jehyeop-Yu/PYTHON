import sys
import cv2
import time
import pyautogui
import numpy as np

template = 'mole.png'
template2 = 'mole_boss.png'

roi_p1 = (50, 160)     # 관심영역(Region Interest, ROI)의 첫번째 지점 좌표(point) -> 튜플 (x1, y1) Of
roi_p2 = (530, 320) # roi의 두번째 point -> 튜플 (x2, y2)

def getImageOfROI( p1, p2 ): # -> roi를 스크린샷으로 찍은 이미지
    im = pyautogui.screenshot(region= p1+p2) # roi를 스크린샷으로 찍음
    return im

def getImageLoc(image, tpl, precision, p1) :
    img_rgb = np.array(image)
    # opencv가 b g r 순서대로 처리하기 떄문에 b 와 r의 순서를 바꿔준다
    b, g, r = cv2.split(img_rgb)
    img_bgr = cv2.merge([r,g,b])

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(tpl, 0) # 0은 cv.IMREAD_GRAYSCALE을 의미
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)    

    position = np.where(res >= precision) # 이미지에서 template의 위치를 받아온다.    
    locations = list()
    for point in zip(*position[::-1]):
        x = point[0] + p1[0]
        y = point[1] + p1[1]
        cv2.circle(img_bgr, point, 1, (0, 0, 255), 1) # 반지름이 1px인 점을 그린다
        abs_pos = x, y
        locations.append(abs_pos)        
    
    # cv2.imwrite('C:/modules/mole_catching/image/captured.png', img_bgr) # result를 저장
        
    return tuple(locations)

def imageClicks(image, pos):
    img = cv2.imread(image)
    height, width, channels = img.shape
    i=1
    for p in pos:
        x = p[0] + width/2
        y = p[1] + height/2
        pyautogui.click( x, y )
        print(i, '번째 클릭')
        i += 1

start_time = time.time()

while True:
    current_time = time.time() # 현재 시간을 받아온다.
    
    if( current_time - start_time > 20.0): # 프로그램을 20초 동안만 실행
        print("Time Out")
        sys.exit(0) # 정상종료 코드
        break  

    source_image = getImageOfROI( roi_p1, roi_p2 ) # im에 roi의 이미지를 저장
    if source_image is None:
        print("Error - can't capture image of ROI")
        sys.exit(1)
    
    pos = getImageLoc(source_image, template, 0.82, roi_p1)
    if pos is ():
        print("image not found", template)
    else:
        print(template, " position : ", pos) 
        imageClicks( template, pos )

    pos = getImageLoc(source_image, template2, 0.82, roi_p1)
    if pos is ():
        print("image not found", template2)
    else:
        print(template2, " position : ", pos) 
        imageClicks( template2, pos )
    time.sleep(0.3) # delay