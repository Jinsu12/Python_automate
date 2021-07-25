import pyautogui
import time

x= 900
y = 302
print1 = 1690,165 # 전체화면 후 인쇄 클릭
print2 = 45,40 # 인쇄 클릭된 이후 다시 누르는 인쇄
page_setting = 61, 382 # 인쇄할 페이지 지정
first_mail = x, y
increase = 21

numb = int(input("몇번째 메일을 출력할지 입력해주세요 >> "))
mult_print = input("연속출력 할까요? '엔터' or 'n' >> ")

'''Functions'''


def full_screen():
    '''창 최대화'''
    time.sleep(1.5)
    pyautogui.moveTo(900, 900, 1)
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(2)
            
            
def choose_page():
    '''인쇄 클릭 후 출력할 페이지 클릭'''
    if page_num == "":
        pyautogui.click(61, 382) #좌측 인쇄 클릭
        time.sleep(1.5)
        pyautogui.press('enter')
    else:
        pyautogui.click(61, 382) #좌측 인쇄 클릭
        time.sleep(1.5)
        pyautogui.typewrite('1-'+ page_num)
        pyautogui.press('enter')


def wait_blank_click():
    time.sleep(1)
    pyautogui.click(900,250)
    time.sleep(0.2)
    

def print_process():
    for i in range(numb2):
        time.sleep(1.5)
        pyautogui.moveTo(900, 900, 1)
        full_screen()
        time.sleep(1.8)
        pyautogui.doubleClick(print1)
        time.sleep(2)
        pyautogui.click(print2)
        time.sleep(1.5)
        choose_page()
        pyautogui.click(900, 300)
        wait_blank_click()


def cont_printing(number):
    if numb <= 1:
        count = 0
        for i in range(numb2):
            print_mail(number+count)
            count += 1
        print_process()

    else:
        count = 0
        for i in range(numb2-numb+1):
            print_mail(number+count)
            count += 1  
        print_process()
            

def print_mail(number):
    wait_blank_click()
    first_mail = x, y+((number-1)*increase)
    pyautogui.click(first_mail)
    print_process()
    time.sleep(4)
    
    
if mult_print == 'n':
    page_num = input("1 페이지는 기본으로 출력합니다, 몇페이지까지 출력할까요? 입력없이 엔터시 한 페이지만 출력 >> ")
    print_mail(numb)


else:
    numb2 = int(input("몇번째 메일까지 출력할까요? >> "))
    page_num = input("1 페이지는 기본으로 출력합니다, 몇페이지까지 출력할까요? 입력없이 엔터시 한 페이지만 출력 >> ")
    cont_printing(numb)
