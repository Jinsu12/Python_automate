
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
print_and_close()  ## print & close 2를 사용했어야 됐나?


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
