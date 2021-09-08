import time
import random

def add_coma(a):
    ans = a
    digit = 0
    real_ans = ''
    while (ans != 0):
        temp = str(ans % 10)
        ans //= 10
        digit += 1
        real_ans = temp + real_ans
        if (digit % 3 == 0) and (ans != 0):
            real_ans = ',' + real_ans
    return real_ans

def problem(digit):
    a = 0
    b = 0
    kind = random.randint(1,10)
    if (digit == 4):
        a = random.randint(10,99)
        b = random.randint(10,99)
    if (digit == 5):
        if (kind % 2 == 0):
            a = random.randint(100,999)
            b = random.randint(10,99)
        else:
            a = random.randint(10,99)
            b = random.randint(100,999)
    if (digit == 6):
        if (kind < 2):
            a = random.randint(1000,9999)
            b = random.randint(10,99)
        elif (kind > 7):
            a = random.randint(10,99)
            b = random.randint(1000,9999)
        else:
            a = random.randint(100,999)
            b = random.randint(100,999)
    if (digit == 7):
        if (kind == 0):
            a = random.randint(10000,99999)
            b = random.randint(10,99)
        elif (kind == 9):
            a = random.randint(10,99)
            b = random.randint(10000,99999)
        elif (kind < 5):
            a = random.randint(100,999)
            b = random.randint(1000,9999)
        else:
            a = random.randint(1000,9999)
            b = random.randint(100,999)
    if (digit == 8):
        if (kind < 2):
            a = random.randint(10000,99999)
            b = random.randint(100,999)
        elif (kind > 7):
            a = random.randint(100,999)
            b = random.randint(10000,99999)
        else:
            a = random.randint(1000,9999)
            b = random.randint(1000,9999)
    print (add_coma(a),'*',add_coma(b),'=?')
    ans = input()
    print(add_coma(a*b))
    if (ans == add_coma(a*b)):
        print('CORRECT')
        if (digit == 4):
            return 1
        else:
            return 2
    print('WRONG')
    return 0

start = time.time()
end = time.time()
score = 0
for i in range (60):
    print('\n\n\n\n\n第',i+1,'題')
    digit = 0
    if (i < 20):
        digit = 4
    elif (i < 40):
        digit = 5
    elif (i < 50):
        digit = 6
    else:
        digit = 7
    temp = problem(digit)
    original = end - start
    end = time.time()
    if (end - start > 180.00):
        end = start + 180
        break
    else:
        score += temp
        print('你這題花了',round(end - start - original,3),'秒')
        print('已經過了',round(end - start,3),'秒')
print('時間到，你總共花了',round(end - start,3),'秒')
print('你的分數是',score,'分。')
