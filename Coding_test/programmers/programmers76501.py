# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):

    real_number = []

    for i in range(len(absolutes)):
        if signs[i] == False:
            real_number.append(absolutes[i] * -1)
        else:
            real_number.append(absolutes[i])
    answer = sum(real_number)
    return answer
