# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

data = input().split()
for i in range(eval(data[1]),eval(data[2])+1):
    a = str(i)
    while len(a) < eval(data[0]):
        a = '0' + a
    print(a)