import pyautogui
import time

# 출력순서 정리

## 팀별 영업집계표
team_sales = 94, 859
## 출하일보
daily_sales = 97, 617
## 회계모듈 부서별 세금계산서
fin_team_tax = 175, 425
## 거래명세표
trade_acc = 88, 641
## 출하현황
ship_status = 120, 671
## 주문서 현황
order_status = 96, 695
## 수금현황
receipt_status = 96, 721
## 기간별 미수금 현황
balance_status = 87, 751



# 기타 버튼 정리

## 리셋버튼
click_reset = 1661, 144
## 빈 공간 클릭
click_blank = 1205, 207
## 출력 미리보기
click_preview = 1802, 141
## 출력하기
click_print = 1305, 217
## 닫기버튼 (출력하기 이후 닫는 버튼)
click_close = 1357, 217



# 함수

## 출력 후 닫기
def print_and_close():
    pyautogui.click(click_preview)
    time.sleep(3) # 출력되는 시간 보고 이후에 더 줄이기
    pyautogui.click(click_print)
    time.sleep(8) # 출력되는 시간 보고 이후에 더 줄이기
    pyautogui.click(click_close)
    time.sleep(1.5)
    pyautogui.click(click_blank)

## 리셋 후 빈공간 누르기
def reset_and_blank():
    pyautogui.click(click_reset)
    time.sleep(0.8)
    pyautogui.click(click_blank)

## 10번 내리기
def ten_down():
    i = 0
    while True:
        pyautogui.press('down')
        i += 1
        if i == 10:
            break

## 50번 내리기
def fifty_down():
    i = 0
    while True:
        ten_down()
        i += 1
        if i == 5:
            break

## 10번 올리기
def ten_up():
    i = 0
    while True:
        pyautogui.press('up')
        i += 1
        if i == 10:
            break
## 50번 올리기
def fifty_up():
    i = 0
    while True:
        ten_up()
        i += 1
        if i == 5:
            break


## 팀별 영업집계표 출력
time.sleep(1)
pyautogui.click(team_sales)
time.sleep(2)
pyautogui.click(click_blank)
time.sleep(0.5)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')