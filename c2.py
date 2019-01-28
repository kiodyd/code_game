# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

times = eval(input())
w_a = 0
w_b = 0
pingshou = ['g g','c c','p p']
a_win = ['g c','c p','p g']
for i in range(0,times):
    game = input()
    if game in pingshou:
        continue
    elif game in a_win:
        w_a = w_a + 1
    else:
        w_b = w_b + 1
print(w_a)
print(w_b)
    
