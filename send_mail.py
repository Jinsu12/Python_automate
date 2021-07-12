import pyautogui
import time

company = int(input("국가순번 입력해주세요 >> "))

def select_company():
    '''select the email of the company'''
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

def paste():
    '''paste'''
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

def copy():
    '''copy'''
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

new_mail = 680,780
empty_space_tocopy = 1750,450
# 새편지 클릭하고 제목복사해서 붙여넣기

pyautogui.click(new_mail)
time.sleep(0.5)
pyautogui.click(new_mail)
time.sleep(3.5)
pyautogui.moveTo(empty_space_tocopy)
# time.sleep(0.5)
pyautogui.moveTo(empty_space_tocopy)
pyautogui.moveTo(1200,350,0.5)
pyautogui.click(x=1200,y=330,button='left')
select_and_copy()
pyautogui.moveTo(300,850)
pyautogui.click(x=300,y=850,button='left')
paste()



#수신인 선택
pyautogui.moveTo(2030,250)
pyautogui.click(x=2030,y=250,button='left')
pyautogui.keyDown('ctrl')
for i in range(4):
    pyautogui.press('right')
pyautogui.press('up')
pyautogui.press('left')
pyautogui.keyUp('ctrl')
pyautogui.keyDown('ctrl') #만나는 문자로 이동
select_company()
pyautogui.press('right')
pyautogui.keyUp('ctrl')
copy()
pyautogui.moveTo(300,650)#붙여넣기
pyautogui.click(x=300,y=740,button='left')
paste()
pyautogui.press('enter')
#내용 복사하기
pyautogui.moveTo(1750,450,1)
pyautogui.click(x=1750,y=450,button='left')
copy()
pyautogui.keyDown('ctrl')
pyautogui.moveTo(230,1010)
pyautogui.click(x=230,y=1010,button='left')
pyautogui.press('pageup')
paste()
pyautogui.press('enter')
# Dear 복사
pyautogui.moveTo(2030,250)
pyautogui.click(x=2030,y=250,button='left')
pyautogui.keyDown('ctrl')
for i in range(4):
    pyautogui.press('right')
pyautogui.press('up')
pyautogui.press('left')
pyautogui.keyUp('ctrl')
pyautogui.keyDown('ctrl') #만나는 문자로 이동
select_company()
pyautogui.press('right')
pyautogui.press('right')
pyautogui.keyUp('ctrl')
copy()
# Dear 붙여넣기
pyautogui.moveTo(1200,220)
pyautogui.click(x=1200,y=220,button='left')
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')
paste()
select_and_copy()
# 메일 내용으로 이동
pyautogui.moveTo(230,1010)
pyautogui.click(x=230,y=1010,button='left')
pyautogui.press('pageup')
pyautogui.press('home')
for i in range(4):
    pyautogui.press('pageup')
paste()
for i in range(2):
    pyautogui.press('enter')
#파일 첨부하기
pyautogui.moveTo(950,250)
pyautogui.mouseDown()
pyautogui.moveTo(700,900)
pyautogui.mouseUp()
