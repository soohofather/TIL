number_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solution(s):
    
    for i in range(len(number_names)):

        s = s.replace(number_names[i], str(i))

    answer = int(s)

    return answer
    
print(solution('123'))