# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import re
input_lines = input()
fault = False
if re.match(r'^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z\d]{6,30}$',input_lines):
    for i in range(0,len(input_lines)-2):
        if input_lines[i] == input_lines[i+1] == input_lines[i+2]:
            fault = True
    if fault:
        print("Invalid")
    else:
        print("Valid")
else:
    print("Invalid")
