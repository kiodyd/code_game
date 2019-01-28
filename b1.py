# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

num = eval(input())
final_word = ''
for word_i in range(0,num):
    word = input()
    sign = -1
    for i in range(0,len(word)):
        if(word[:i+1]==final_word[-1-i:]):
            sign = i
    final_word = final_word + word[sign+1:]

print(final_word)