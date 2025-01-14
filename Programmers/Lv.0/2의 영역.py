arr = [1,2,1,2,1,10,2,1]

def solution(arr):
    if 2 not in arr:
        return [-1]
    first2 = arr.index(2)
    last2 = len(arr) - arr[::-1].index(2)
    return arr[first2:last2]


def solution2(arr):
    if 2 not in arr:
        return [-1]
    index2 = [i for i,n in enumerate(arr) if n == 2]
    result = arr[index2[0]:index2[-1]+1]
    return result