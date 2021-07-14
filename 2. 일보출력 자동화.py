# import pyautogui
# import time

# today = input('오늘날짜 입력: 예) 20210708 >> ')

# ## 팀별 영업집계표
# team_sales = 117, 586
# ## 출하일보
# daily_sales = 88, 615
# ## 회계모듈 부서별 세금계산서
# fin_team_tax = 175, 425
# ## 거래명세표
# trade_acc = 94, 644
# ## 출하현황
# ship_status = 92, 668
# ## 주문서 현황
# order_status = 91, 695
# ## 수금현황
# receipt_status = 96, 721
# ## 기간별 미수금 현황
# balance_status = 85, 750
# ## 거래처별 미수금 현황
# comp_balance = 907,271
# ## 정렬
# sort_balance = 1288, 398

# # 기타 버튼 정리

# ## 리셋버튼
# click_reset = 1661, 144
# ## 출력 미리보기
# click_preview = 1802, 141
# ## 출력하기
# click_print = 1305, 217
# ## 닫기버튼 (출력하기 이후 닫는 버튼)
# click_close = 1357, 217
# # 출력크기 맞춤
# click_fit_size = 787, 219
# # SEL 선택
# click_sel = 340, 255
# # 결재창 클릭
# click_table=1050, 218
# ## 빈 공간 클릭
# click_blank = 1893, 180



# # 모듈이동
# ##메뉴클릭
# change_module1 = 1885, 52
# ##1번 모듈 클릭
# change_module2 = 1827, 95



# # 함수

# def change_module():
#     '''모듈을 변경해주는 함수'''
#     pyautogui.click(change_module1)
#     time.sleep(1)
#     pyautogui.click(change_module2)
#     time.sleep(10)


# def print_and_close():
#     """출력 미리보기 누른 후 인쇄 후 인쇄창 닫아주는 함수"""
#     pyautogui.click(click_preview)
#     time.sleep(3)  # 출력되는 시간 보고 이후에 더 줄이기
#     #     pyautogui.click(click_print)
#     time.sleep(8)  # 출력되는 시간 보고 이후에 더 줄이기
#     pyautogui.click(click_close)
#     time.sleep(1.5)
#     pyautogui.click(click_blank)


# def fit_and_print():
#     '''용지크기에 맞춘 후 출력해주는 함수'''
#     pyautogui.click(click_preview)
#     time.sleep(2)  # 출력되는 시간 보고 이후에 더 줄이기
#     pyautogui.click(click_fit_size)
#     #     pyautogui.click(click_print)
#     time.sleep(8)  # 출력되는 시간 보고 이후에 더 줄이기
#     pyautogui.click(click_close)
#     time.sleep(1.5)
#     pyautogui.click(click_blank)


# def reset_and_blank():
#     """리셋 누른 후 빈공간 눌러주는 함수"""
#     pyautogui.click(click_reset)
#     time.sleep(0.8)
#     pyautogui.click(click_blank)


# def ten_down():
#     for i in range(1,11):
#         pyautogui.press('down')
    

# def fifty_down():
#     for i in range(1, 6):
#         ten_down()
    

# def ten_up():
#     for i in range(1, 11):
#         pyautogui.press('up')
    

# def fifty_up():
#     for i in range(1, 51):
#         pyautogui.press('up')


# def find():
#     '''FIND'''
#     pyautogui.hotkey('ctrl', 'f')


# def five_tab():
#     '''tab키 5번'''
#     for i in range(1, 6):
#         pyautogui.press('tab')
    
# def d_tab():
#     '''tab키 2번'''
#     for i in range(2)
#         pyautogui.press('tab')


# def sort_balance2():
#     '''내림차순으로 바꿔주는 함수'''
#     pyautogui.rightClick(sort_balance)
#     time.sleep(0.3)
#     for i in range(1, 7):
#         pyautogui.press('down')
#     time.sleep(0.5)
#     pyautogui.press('right')
#     time.sleep(0.5)
#     pyautogui.press('down')
#     pyautogui.press('enter')


'''팀별 영업집계표 출력'''
    
## 팀별 영업집계표 출력
time.sleep(1)
# pyautogui.click(team_sales)
# time.sleep(2.5)
pyautogui.click(click_blank)
time.sleep(0.5)
d_tab()
time.sleep(0.5)
pyautogui.press('down')
time.sleep(0.5)
find()
time.sleep(2)
print_and_close()



# '''출하일보 출력'''
# ## 출하일보
# pyautogui.click(daily_sales)
# time.sleep(2.5)
# pyautogui.click(click_blank)
# find()
# time.sleep(4)
# fit_and_print()

# change_module()




# '''회계모듈이동'''
# change_module()


# '''부서별 세금계산서 출력'''

# # 회계모듈 부서별 세금계산서

# pyautogui.click(fin_team_tax)
# time.sleep(2.5)
# pyautogui.click(click_blank)
# time.sleep(1)
# pyautogui.press('tab')
# time.sleep(1)
# for i in range(84):
#     pyautogui.press('up')
# time.sleep(1)
# find()
# time.sleep(1)
# print_and_close()


# '''영업모듈로 이동'''
# change_module()



# '''거래명세표 출력'''
# ## 거래명세표
# pyautogui.click(trade_acc)
# time.sleep(3)
# pyautogui.click(click_blank)
# time.sleep(1)
# five_tab()
# d_tab()
# pyautogui.press('down')
# time.sleep(1)
# pyautogui.click(click_table)
# time.sleep(1)
# find()
# time.sleep(4.5)
# pyautogui.click(click_sel)
# time.sleep(1)
# print_and_close()


# '''출하현황 출력'''

# # 출하현황
# pyautogui.click(ship_status)
# time.sleep(3)
# pyautogui.click(click_blank)
# time.sleep(1)
# for i in range(3):
#     pyautogui.press('tab')
# time.sleep(0.3)
# pyautogui.press('down')
# time.sleep(0.3)
# for i in range(16):
#     pyautogui.press('tab')
# pyautogui.press('down')
# find()

# time.sleep(5)
# fit_and_print()
# time.sleep(3)


# '''주문서 현황 출력'''
# ## 주문서 현황
# time.sleep(1)
# pyautogui.click(order_status)
# time.sleep(2.5)
# pyautogui.click(click_blank)
# for i in range(3):
#     pyautogui.press('tab')
# pyautogui.press('down')
# find()

# time.sleep(2)
# fit_and_print()
# time.sleep(3)




# '''수금현황 출력'''
# # 수금현황
# time.sleep(1)
# pyautogui.click(receipt_status)
# time.sleep(2.5)
# pyautogui.click(click_blank)
# d_tab()
# pyautogui.press('down')
# time.sleep(1)
# d_tab()
# d_tab()
# time.sleep(1)
# pyautogui.typewrite(today)
# find()
# time.sleep(2.5)
# print_and_close()
# time.sleep(3)



  
# '''기간별 미수금 현황 출력'''
# # # 기간별 미수금 현황
# pyautogui.click(click_blank)
# pyautogui.click(balance_status)
# time.sleep(1)
# pyautogui.click(click_blank)
# time.sleep(0.5)
# d_tab()
# time.sleep(0.5)
# pyautogui.press('down')
# time.sleep(0.5)
# d_tab()
# for i in range (1, 25):
#     pyautogui.press('down')
# pyautogui.press('tab')
# pyautogui.press('down')
# pyautogui.press('down')
# pyautogui.click(comp_balance)
# time.sleep(1)
# find()
# time.sleep(5)
# sort_balance2()
# time.sleep(0.8)
# fit_and_print()
# time.sleep(3)




'''여기부터 패키징'''
## 팀별 영업집계표 출력
# time.sleep(1)
# pyautogui.click(team_sales)
time.sleep(2.5)
pyautogui.click(click_blank)
time.sleep(0.5)
d_tab()
time.sleep(0.5)
for i in range(3):
    pyautogui.press('down')
time.sleep(0.5)
find()
time.sleep(2)
print_and_close()


'''회계모듈이동'''
change_module()


'''부서별 세금계산서 출력'''

# 회계모듈 부서별 세금계산서

pyautogui.click(fin_team_tax)
time.sleep(2.5)
pyautogui.click(click_blank)
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
for i in range(3):
    pyautogui.press('down')
time.sleep(1)
find()
time.sleep(1)
print_and_close()


'''영업모듈로 이동'''
change_module()


'''거래명세표 출력'''
## 거래명세표
pyautogui.click(trade_acc)
time.sleep(3)
pyautogui.click(click_blank)
time.sleep(1)
five_tab()
d_tab()
for i in range(3):
    pyautogui.press('down')
time.sleep(1)
pyautogui.click(click_table)
time.sleep(1)
find()
time.sleep(4.5)
pyautogui.click(click_sel)
time.sleep(1)
print_and_close()


'''출하현황 출력'''

# 출하현황
pyautogui.click(ship_status)
time.sleep(3)
pyautogui.click(click_blank)
time.sleep(1)
for i in range(3):
    pyautogui.press('tab')
time.sleep(0.3)
pyautogui.press('down')
pyautogui.press('down')
time.sleep(0.3)
for i in range(16):
    pyautogui.press('tab')
pyautogui.press('down')
find()

time.sleep(5)
fit_and_print()
time.sleep(3)



'''주문서 현황 출력'''
## 주문서 현황
time.sleep(1)
# pyautogui.click(order_status)
# time.sleep(2.5)
pyautogui.click(click_blank)
for i in range(3):
    pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
find()

time.sleep(2)
fit_and_print()
time.sleep(3)


'''수금현황 출력'''
# 수금현황
time.sleep(1)
# pyautogui.click(receipt_status)
# time.sleep(2.5)
pyautogui.click(click_blank)
d_tab()
pyautogui.press('down')
pyautogui.press('down')
time.sleep(1)
d_tab()
d_tab()
time.sleep(1)
pyautogui.typewrite(today)
find()
time.sleep(2.5)
print_and_close()
time.sleep(3)


'''기간별 미수금 현황 출력'''
# # 기간별 미수금 현황
pyautogui.click(click_blank)
pyautogui.click(balance_status)
time.sleep(1)
pyautogui.click(click_blank)
time.sleep(0.5)
d_tab()
time.sleep(0.5)
pyautogui.press('down')
pyautogui.press('down')
time.sleep(0.5)
d_tab()
for i in range (1, 25):
    pyautogui.press('down')
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.click(comp_balance)
time.sleep(1)
find()
time.sleep(5)
sort_balance2()
time.sleep(0.8)
fit_and_print()
time.sleep(3)
