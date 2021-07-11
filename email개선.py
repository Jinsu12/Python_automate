import time
import pyautogui

x = 900
y = 302

print_email1 = x, y
print_email2 = x, y+21
print_email3 = x, y+42
print_email4 = x, y+63
print_email5 = x, y+84
print_email6 = x, y+105
print_email7 = x, y+126
print_email8 = x, y+147
print_email9 = x, y+168
print_email10 = x, y+189
print_email11 = x, y+210
print_email12 = x, y+231
print_email13 = x, y+252
print_email14 = x, y+273
print_email15 = x, y+294
print_email16 = x, y+315
print_email17 = x, y+336
print_email18 = x, y+357
print_email19 = x, y+378
print_email20 = x, y+399
print_email21 = x, y+420
print_email22 = x, y+441
print_email23 = x, y+462
print_email24 = x, y+483
print_email25 = x, y+504
print_email26 = x, y+525
print_email27 = x, y+546
print_email28 = x, y+567
print_email29 = x, y+588
print_email30 = x, y+609
print_email31 = x, y+630
print_email32 = x, y+651
print_email33 = x, y+672
print_email34 = x, y+693
print_email35 = x, y+714
print_email36 = x, y+735
print_email37 = x, y+756
print_email38 = x, y+777
print_email39 = x, y+798
print_email40 = x, y+819
print_email41 = x, y+840
print_email42 = x, y+861
print_email43 = x, y+882
print_email44 = x, y+903
print_email45 = x, y+924
print_email46 = x, y+945
print_email47 = x, y+966
print_email48 = x, y+987
print_email49 = x, y+1008
print_email50 = x, y+1029




'''Functions'''
def full_screen():
    '''창 최대화'''
    time.sleep(1.5)
    pyautogui.moveTo(900, 900, 1)
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(2)

def click_print():
    pyautogui.doubleClick(1690, 165) #최대화된 메일의 우측에 있는 인쇄 클릭
    time.sleep(2)

def choose_page():
    '''인쇄 클릭 후 출력할 페이지 클릭'''
    pyautogui.click(45, 40) #좌측 인쇄 클릭
    time.sleep(1.5)
    if page_num == "":
        pyautogui.press('enter')
    else:
        pyautogui.typewrite('1-'+ page_num)

# click_newmail() #새편지 클릭 후 최대화
# click_print() # 인쇄 클릭
# choose_page() # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
# pyautogui.click(900, 300)
# time.sleep(1)
# pyautogui.click(900, 250)
# time.sleep(1)


email_numbers = input("몇번째 메일까지 출력할까요? >> ")
page_num = input("1 페이지는 기본으로 출력합니다, 몇페이지까지 출력할까요? 입력없이 엔터시 한 페이지만 출력 >> ")


if email_numbers == 1:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 2:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 3:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 4:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 5:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 6:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email6)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 7:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email6)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email7)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 8:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email6)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email7)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email8)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 9:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email6)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email7)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email8)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email9)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 10:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email6)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email7)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email8)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email9)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email10)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

elif email_numbers == 11:
    pyautogui.click(print_email1)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email2)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email3)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email4)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email5)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email6)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email7)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email8)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email9)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email10)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)

    pyautogui.click(print_email11)
    full_screen()
    click_print()  # 인쇄 클릭
    choose_page()  # 인쇄 클릭 후 인쇄할 페이지 지정 후 출력
    pyautogui.click(900, 300)
    time.sleep(1)
    pyautogui.click(900, 250)
    time.sleep(1)