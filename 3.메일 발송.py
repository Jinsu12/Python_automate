import pyautogui
import time

company = int(input("국가순번 입력해주세요 >> "))

'''새편지 클릭 위치'''
new_mail = 680,780 # 새편지 위치

'''기존 메일 빈공간 클릭 (좌측모니터에 절반 사이즈로 우측에)'''
empty_space_tocopy = 1750,450 #메일 내용을 복사하기 위해 메일 빈공간 클릭 위치
title = 1183,336 #제목 복사
#수신인 복붙하기 위함
old_mail =1200,220


'''엑셀파일 위치 (최대화로 오른쪽 모니터에)'''
excel_position = 2030,250 # 엑셀파일 위치


'''신규 메일 (1/4 사이즈로 왼쪽 모니터 좌측 하단에)'''
sending_mail = 230,1010 # 보내는 메일의 내용 클릭 좌표
new_title = 300,850 #제목 붙여넣기
receiver = 300, 740



'''파일 드롭위치'''
pick_point = 950, 250 # 첨부파일 픽업 위치
drop_point = 700, 900 # 첨부파일 드롭 위치



def starting_point():
    '''엑셀 시작 위치로 이동 셀 A1로'''
    pyautogui.keyDown('ctrl')
    for i in range(4):
        pyautogui.press('right')
    pyautogui.press('up')
    pyautogui.press('left')
    pyautogui.keyUp('ctrl')

def pick_drop():
    '''첨부파일 드래그 앤 드롭'''
    pyautogui.moveTo(pick_point)
    pyautogui.mouseDown()
    pyautogui.moveTo(drop_point)
    pyautogui.mouseUp()

def select_company():
    '''엑셀파일에서 메일보낼 업체 선택'''
    for i in range(1, company+1):
        pyautogui.press('down')
        
def select_and_copy():
    '''select all and copy'''
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def copy():
    '''copy'''
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def paste():
    '''paste'''
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')


def click_newmail():
    '''새 편지 클릭'''
    pyautogui.click(new_mail)
    time.sleep(0.5)
    pyautogui.click(new_mail)
    time.sleep(3.5)

def select_all():
    '''ctrl + a'''
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')

# 새편지 클릭하고 제목복사해서 붙여넣기
click_newmail() # 새편지 클릭
pyautogui.moveTo(empty_space_tocopy) # 메일 내용을 복사하기 위해서 빈 공간 클릭
time.sleep(0.5)
pyautogui.moveTo(empty_space_tocopy) # 메일 내용을 복사하기 위해서 빈 공간 클릭
pyautogui.click(empty_space_tocopy)
time.sleep(0.3)
pyautogui.click(title)
select_and_copy()
pyautogui.click(new_title)
paste()



#수신인 선택
pyautogui.click(excel_position) # 엑셀 클릭
starting_point()
pyautogui.keyDown('ctrl') # 만나는 문자로 이동
select_company()
pyautogui.press('right')
pyautogui.keyUp('ctrl')
copy()
pyautogui.click(receiver)
paste()
pyautogui.press('enter')


#메일 본문 내용 복사하기
time.sleep(1)
pyautogui.click(empty_space_tocopy)
copy()
pyautogui.keyDown('ctrl')
pyautogui.click(sending_mail)
pyautogui.press('pageup')
paste()
pyautogui.press('enter')
time.sleep(0.3)


# Dear 복사
pyautogui.click(excel_position) # 엑셀 클릭
starting_point()
pyautogui.keyDown('ctrl') #만나는 문자로 이동
select_company()
pyautogui.press('right')
pyautogui.press('right')
pyautogui.keyUp('ctrl')
copy()


# Dear 붙여넣기
pyautogui.click(old_mail)
select_all()
paste()
select_and_copy()


# 메일 내용으로 이동
pyautogui.click(sending_mail)
pyautogui.press('pageup')
pyautogui.press('home')
for i in range(4):
    pyautogui.press('pageup')
paste()
for i in range(2):
    pyautogui.press('enter')


#파일 첨부하기
pick_drop()


