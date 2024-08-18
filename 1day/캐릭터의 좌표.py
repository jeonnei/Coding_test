# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    answer = [0,0]
    left = [-1,0]
    right = [1,0]
    up = [0,1]
    down = [0,-1]
    for i in keyinput:
        #print(i)
        if i == "left":
            answer=[x+y for x, y in zip(answer,left)]
        elif i == "right":
            answer=[x+y for x, y in zip(answer,right)]
        elif i == "up":
            answer=[x+y for x, y in zip(answer,up)]
        elif i == "down":
            answer=[x+y for x, y in zip(answer,down)]
        if abs(int(board[0]/2))<=abs(answer[0]):
            if answer[0]<0:
                answer[0] = -int(board[0]/2)
            else:
                answer[0]=int(board[0]/2)
        if abs(int(board[1]/2))<=abs(answer[1]):
            if answer[1]<0:
                answer[1] = -int(board[1]/2)
            else:
                answer[1]=int(board[1]/2)
    return answer