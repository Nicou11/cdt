board = [["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"],
 ["orange", "orange", "red", "blue"]]
h = 1
w = 1


def solution(board, h, w):
    answer = 0
    color = board[h][w]
    if h + 1 < len(board) and board[h+1][w] == color:
        answer += 1
    if w + 1 < len(board) and board[h][w+1] == color:
        answer += 1
    if h > 0 and color == board[h-1][w]:
        answer += 1
    if w > 0 and color == board[h][w-1]:
        answer += 1
    print(len(board))
    return answer

print(solution(board, h, w))