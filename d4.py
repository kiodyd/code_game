# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_lines = input()
odd = False
def a(x):
    global odd
    odd = not odd
    return odd
result = ''.join(list(filter(a, input_lines)))
print(result)
