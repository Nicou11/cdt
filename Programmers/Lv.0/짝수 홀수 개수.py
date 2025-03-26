num_list = [1, 2, 3, 4, 5]	#[2, 3]
#num_list = [1, 3, 5, 7]	#[0, 4]

def solution(num_list):
    e = 0
    o = 0
    for i in num_list:
        if i%2 == 0:
            e += 1
        else:
            o += 1
    return [e,o]

#다른 풀이
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
#인덱싱을 이용하여 개수 count
