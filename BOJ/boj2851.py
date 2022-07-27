import sys

sys.stdin = open('boj2851.txt')

result = int(input())                                   # 첫번째 수를 result 에 넣고

for i in range(0,9):
    n = int(input())                                    # 두번째 수부터 9번 돌리는 반복문
    if abs(result - 100) >= abs(result + n - 100):      # 현재 result 값에 빼기 100한 숫자의 절대값과 이번에 더하려는 숫자를 더한 뒤 빼기 100한 숫자의 결과를 비교
        result += n                                     # 만약에 더하려는 숫자를 더한 뒤 절대값이 더 작으면 = 100과 더 가깝다는 뜻으로 result에 숫자를 더함
    else:
        print(result)                                   # 만약에 더하려는 숫자를 더한 뒤 숫자의 절대값이 더 크면 = 100과 더 멀어진다는 뜻으로 더하지 않고 끝냄
        break
else:
    print(result)                                       # 10개의 숫자가 모두 돌았는데 점점 더 100가 가까워져서 바로 위의 if문에서 브레이크가 안걸릴 경우 현재의 result 값을 출력

