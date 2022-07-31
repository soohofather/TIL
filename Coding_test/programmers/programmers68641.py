# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(0, len(numbers) - 1):                # 순서대로 끝에서 두번째까지 돌리는 반복문
        for ii in range(i + 1, len(numbers)):           # 내려온숫자와, 그다음숫자를 더하는 반복문
            answer.append(numbers[i] + numbers[ii])     # 위에서 더한 숫자를 answer에 추가
            answer = sorted(list(set(answer)))          # 정렬 및 중복 제거
    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))