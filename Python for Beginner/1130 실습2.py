#함수선언

def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")

    if button == 1:
        print("#3. (자동으로) 보통커피를 탄다.")
    elif button == 2:
        print("#3. (자동으로) 설탕커피를 탄다.")
    elif button == 3:
        print("#3. (자동으로) 블랙커피를 탄다.")
    else:
        print("#3. (자동으로) 아무거나 탄다.\n")

    print("#4. (자동으로) 물을 붓는다.")
    print("#5. (자동으로) 스푼을 젓는다.")
    print()

#메인
while True:
    name = input("이름이 어떻게 되나요? ")
    coffee = int(input("%s 손님, 어떤 커피를 드릴까요? (1: 보통, 2:설탕, 3: 블랙)" %name))
    coffee_machine(coffee)
    print("%s 손님~ 커피 여기 있습니다." %name)
    Y_N = input("계속 하시겠습니까?(Y/N)")
    if (Y_N == "N") or (Y_N == "n"):
        break

''' if (Y_N != "Y") and (Y_N != "y"):
        break
'''
        
