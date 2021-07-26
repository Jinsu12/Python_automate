import pyautogui
import time

x= 900
y = 302
print1 = 1690,165 # 전체화면 후 인쇄 클릭
print2 = 45,40 # 인쇄 클릭된 이후 다시 누르는 인쇄
page_setting = 61, 382 # 인쇄할 페이지 지정
first_mail = x, y
increase = 21 # 메일별 증가값, 다음 메일을 클릭하기 위해 증가되는 y 값


def full_screen():
    '''창 최대화'''
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')

    
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
    

select = input("선택 출력은 '1'을 연속 출력은 '엔터'를 입력해주세요 >> ")


if select == 1:
    mail_select = int(input("출력할 메일 번호를 입력해주세요"))
    page_num = input("1 페이지는 기본으로 출력합니다, 몇페이지까지 출력할까요? 입력없이 엔터시 한 페이지만 출력 >> ")
    wait_blank_click()
    pyautogui.click(x, (y+(increase*(mail_select-1))))
    print_process()
    
else:
    mail_select = int(input("출력할 메일 번호를 입력해주세요"))
    mail_select2 = int(input("몇번 메일까지 출력할까요?"))
    page_num = input("1 페이지는 기본으로 출력합니다, 몇페이지까지 출력할까요? 입력없이 엔터시 한 페이지만 출력 >> ")
    num_increase = (mail_select-1)*21
    for i in range(mail_select2 - mail_select+1):
        pyautogui.click(x, y+num_increase)
        print_process()
        num_increase += 21
    
print("####출력이 완료되었습니다####")
