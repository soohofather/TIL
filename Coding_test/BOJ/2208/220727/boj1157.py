alphas = input().upper()
new_alphas = set(alphas)                # 시간 초과떠서 입력 값 알파벳 중복 제거 추가

cnt1 = 0
result = ''
cnt2 = 0 

for i in new_alphas:                    # 중복 제거된 알파벳을 하나하나 돌려서 그 알파벳이 입력값에 몇개가 있는지 비교
    if alphas.count(i) > cnt1:          # 만약에 찾은 값이 기존 값보다 크면 cnt1에 갯수를, result에 그 알파벳을 넣음
        cnt1 = 0
        result = ''
        cnt1 += alphas.count(i)         
        result += i
    elif alphas.count(i) == cnt1:       # 만약에 찾은 값이 기존값과 동일한 경우에는 cnt2에다가 갯수만 추가
        cnt2 = 0
        cnt2 += alphas.count(i)

print(result if cnt1 != cnt2 else '?')  # cnt1 과 cnt2가 같다면 가장 큰 숫자가 두개 이상이라는 것을 의미하여 이때만 ? 출력하고 나머진 result에 입력된 알파벳 출력