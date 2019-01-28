data = input().split()
x = 0
y = 0

def U():
    global y
    y = y + 1
def D():
    global y
    y = y - 1
def R():
    global x
    x = x + 1
def L():
    global x
    x = x - 1
    
for i in range(0,eval(data[2])):
    ii = input()
    if ii == 'U':
        U()
    if ii == 'D':
        D()
    if ii == 'R':
        R()
    if ii == 'L':
        L()

if x >= 0 and y >= 0 and x<= eval(data[0]) and y <= eval(data[1]):
    print("valid")
else:
    print("invalid")