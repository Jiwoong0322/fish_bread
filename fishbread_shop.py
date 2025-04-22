#주문, 관리자, 종료 이 3가지 선택을 통해 각각 기능ㅇ이 작동되도록 만들것
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있다.

stock = { # key값을 이용해서 value, 딕셔너리를 써야하는 상황은 어떤 스토리 기반으로 데이터가 구성되었을때    
    "팥붕어빵": 10,
    "슈크림붕어빵": 10,
    "초코붕어빵": 10,
    "피자붕어빵": 10,
    "김치붕어빵": 10,
}

sales = {
    "팥붕어빵": 0,
    "슈크림붕어어빵": 0,
    "초코붕어빵": 0,
    "피자붕어빵": 0,
    "김치붕어빵": 0
}

def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요.\n팥붕어빵\n슈크림붕어빵\n초코붕어빵\n피자붕어빵\n김치붕어빵\n만약 뒤로가기를 원하신다면 '뒤로가기'를 입력해주세요\n")
        if bread_type in stock: #"팥붕어빵" or "슈크림붕어빵" or "초코붕어빵" or "피자붕어빵" or "김치붕어빵":
            print(f"현재 {bread_type}의 재고는 {stock[bread_type]}개입니다.\n")
            order = input("주문하시겠습니까? Y/N\n")
            if order == "Y":
                bread_count = int(input("수량을 입력하여주십시오\n"))
                if bread_count <= stock[bread_type]:
                    stock[bread_type] -= bread_count
                    sales[bread_type] += bread_count
                    print(f"{bread_type} {bread_count}개를 주문하셨습니다. 감사합니다!\n")
                else:
                    print("재고가 부족합니다. 다시 시도해주세요\n")
            elif order == "N":
                print("이전 화면으로 돌아갑니다.\n")
            else:
                print("잘못된 입력입니다.\n")
        elif bread_type == "뒤로가기":
            print("이전 화면으로 돌아갑니다\n")
            break
        else:
            print("잘못된 입력입니다.\n")
            break


while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료): ")
    if mode == "종료":
        break
    elif mode == "관리자":
        admin_mode()
    elif mode == "주문":
        order_bread()

print("시스템이 종료되었습니다.")