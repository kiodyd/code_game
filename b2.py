# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

num = eval(input())
max_score = [0,0,0,0,0]
for i in range(1,num+1):
    temp_score = [i,0,0,0,0]
    data = input()
    for r in data:
        if r == 'W':
            temp_score = [temp_score[0],2+temp_score[1],1+temp_score[2],temp_score[3],temp_score[4]]
        elif r == 'D':
            temp_score = [temp_score[0],1+temp_score[1],temp_score[2],1+temp_score[3],temp_score[4]]
        elif r == 'L':
            temp_score = [temp_score[0],temp_score[1],temp_score[2],temp_score[3],1+temp_score[4]]
    if max_score[1]<temp_score[1]:
        max_score = temp_score
max_score = (' ').join([str(x) for x in max_score])
print(max_score)
    
    