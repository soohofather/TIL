T = int(input())

for i in range(0, T):           # 0번부터 T번 까지 돌아가는 반복문
    oxox = input()              # oxox 데이터 넣기
    cnt = 0
    result = 0
    for ii in oxox:                 # o면 출력할 값에 1을 더하고, 다음 o면 2를 더해야하니까 cnt에다가 1을 더해서 다음이 o면 2를 더하게 만듬
            if ii == 'O':
                cnt += 1
                result += cnt
            else:
                cnt = 0             # x면 cnt를 0으로 만들어서 다음 첫 o에 1을 더하게끔 만듬
    print(result)