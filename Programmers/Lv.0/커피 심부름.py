order = ["cafelatte", "americanoice", "hotcafelatte", "anything"]

def solution(order):
    answer = 0
    for j in order:
        if "americano" in j:
            answer += 4500
        elif "latte" in j:
            answer += 5000
        elif j == "anything":
            answer += 4500
    return answer


# 다른 풀이
def solution2(order):
    answer = 0
    for want in order:
        if 'latte' in want:
            answer += 500
        answer += 4500
    return answer

print(solution2(order))