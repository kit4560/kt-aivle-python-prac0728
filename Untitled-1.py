# -*- coding: utf-8 -*-
import numpy as np
# import h5py
# import matplotlib.pyplot as plt

def amIRoot(num):
    new_num = int(num / 2) 
    for i in range(2, new_num):
        if i * i == num:
            return int((i+1)**2)
    return -1

def lucky(score):
    new_score = str(score)
    length = len(new_score)
    if length % 2 != 0:
        print("입력 안되는 숫자.")
    else:
        left = 0
        right = 0
        for i in range(length):
            if i < length/2:
                left = left + int(new_score[i])
            else:
                right = right + int(new_score[i])
        if left == right:
            print("LUCKY")
        else:
            print("READY")


def max_string(num_str):
    length = len(num_str)
    number = 0
    multi = 1
    for i in range(length):
        if int(num_str[i]) == 1:
            number = number + 1
        elif int(num_str[i]) >= 2:
            multi = multi * int(num_str[i])
    return number + multi

def measure_plus(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count = count + 1
        if count % 2 == 0:
            answer = answer + i
        else:
            answer = answer - i
    return answer


def new_number(num):
    if num > 100:
        return 0
    else:
        num_cpy = str(num)
        how_many = 0
        if len(num_cpy) == 1:
            num_cpy = str('0')+str(num_cpy)
        while(1):
            how_many = how_many + 1
            num_cpy = str(num_cpy[1]) + str(int(num_cpy[0]) + int(num_cpy[1]))[-1]
            if int(num_cpy) == num:
                break
        return how_many

def common_multiple(num1, num2):
    return int((num1 * num2) / common_factor(num1, num2))

def common_factor(num1, num2):
    min = np.min((num1,num2))
    for i in range(2, min+1):
        if num1 % i == 0 and num2 % i == 0:
            factor = i
    return factor

def look_loot(num):
    for root in range(2, num-1):
        pwd = 0
        m = num
        while(1):
            m = m / root
            pwd = pwd + 1
            if pwd == 7:
                break
            if m == 1:
                print(root, pwd)
                break
            else:pass

def electricPay(power):
    pay_basic = [410, 910, 1600]
    pay_power = [60.7, 125.9, 187.9]
    money = 0

    if power > 100:
        if power < 200:
            p = 1
        else:
            p = 2
    else :
        p = 0
    print(p)
    money = money + pay_basic[p]
    for i in range(p+1):
        if power > 100:
            m = 100
        else:
            m = 100-power
        money = money + m * pay_power[i]
        power = power - 100
        if power <= 0:
            break
    money = money + int(money * 0.1) + int(money * 0.037)
    print(money)

def print_plus_mi(num):
    for i in range(num):
        if i % 2 == 0:
            print("+", end="")
        else:
            print("-", end="")
    print('')

def rect_on_print(sizeOfRect):
    for i in range(1, sizeOfRect+1):
        if sizeOfRect % i == 0:
            print(str(i) + " x " + str(int(sizeOfRect/i)))

def plus_on_print(x, y):
    if x > y:
        x, y = y, x
    else:
        pass
    sum = 0
    for i in range(x, y+1):
        sum = sum + i
        if i != y:
            print(i, end = '+')
        else:
            print(i, end = '=')
            print(sum)


def waterPay(L, company):
    pay_A = 100
    pay_B = [150, 75]
    over_B = 50

    if company == 'A':
        return L * pay_A
    elif company == 'B':
        if L > over_B:
            return L * pay_B[1]
        else:
            return L * pay_B[0]

def f():
    pass
    """a = []
    b = []
    for i in range(7):
        a.append(int(input("숫자 입력.")))
    max = np.max(np.array(a))
    for i in range(len(a) - 1):
        min = np.min(np.array(a))
        b.append(min)
        a.remove(min)
    b.append(max)
    print(a)
    print(b)
    print("중앙값은 : "+str(b[len(b)//2]))"""

    """nums = []
    while(1):
        n = input("숫자 입력. 문자 입력시 종료.")
        try:
            n = int(n)
            nums.append(n)
        except:
            break
    max = int(nums[0])
    for i in range(len(nums)):
        if int(nums[i]) > max:
            max = int(nums[i])
    print(max)
    # print(np.max(np.array(nums)))"""

    """a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))

    max = a
    if b > max :
        max = b
    if c > max : 
        max = c
    if d > max:
        max = d
    print("max = "+str(max))"""

f();
print(amIRoot(int(input("숫자 입력 : "))))
# lucky(int(input("숫자입력 : ")))
# print(max_string("02984"))
# print(measure_plus(24,27))
# print(new_number(int(input("숫자입력 : "))))
# print(common_multiple(12, 16))
# print(common_factor(24, 32))
# look_loot(int(input("number : ")))
# electricPay(250)
# print_plus_mi(12)
# rect_on_print(int(input("직사각형의 넓이를 입력하세요. : ")))

"""a = int(input("x = "))
b = int(input("y = "))

plus_on_print(a, b)"""

"""howmany = int(input("얼마나 사용하셨나요?"))
com = input("사용 회사는?")
print("이번달 요금은 "+ str(waterPay(howmany, com)) +"원 입니다.")"""

"""i = [1, 2, 3, 4, 5]
for [index, x] in enumerate(i):
    print('Hello World x ' + str(index + 1));"""

"""stop = False
while(stop != 1):
    name = input("이름을 입력하세요.")
    print("안녕하세요. " + name)
    num = input("종료하려면 1 입력.")
    try:
        num = int(num)
        if num == 1:
            stop = True
            print("종료")
    except:
        print("숫자만 입력해주세요.")"""

# print(np.abs(-4))
# print(h5py.__version__)