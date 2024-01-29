# day 2/366

def solution(string):
    # return string[::-1]
    temp = list(string)
    temp.reverse()
    return ''.join(temp)

print(solution("testos"))