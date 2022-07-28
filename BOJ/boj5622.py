phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

button = input()
time = 0


for i in button:                            # input 값을 하나하나 던짐. WA면 W 던지고 A 던지고
    for ii in phone:                        # 위에서 던진 값이 목록에서 index 몇에 있는지 확인 W는 phone 인덱스 7에 위치
        if i in ii:
            time += phone.index(ii) + 3     # 초는 위치 + 3이니까 인덱스 7에 3을 더해서 W는 10초
print(time)