num=input("16진수 한 글자 입력:")

if(num>= '0' and num <= '9') or (num>='a' and num <= 'f') or (num>= 'A' and num <= 'F'):
    print("10진수==>", int(num,16))
else:
    print("16진수가 아닙니다.")
    
