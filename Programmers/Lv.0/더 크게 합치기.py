a = 9
b = 91

def solution(a, b):
    answer = 0
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    if ab > ba:
        return int(ab)
    else:
        return int(ba)

# 다른 풀이
def solution2(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))