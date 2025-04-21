#주문, 관리자, 종료 이 3가지 선택을 통해 각각 기능ㅇ이 작동되도록 만들것
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있다.

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    if mode == "종료":
        break
    elif mode == "관리자":
        order_bread()
    elif mode == "주문":
        admin_mode()

print("시스템이 종료되었습니다.")