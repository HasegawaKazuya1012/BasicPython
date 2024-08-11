# TODO
#import math
#xとyをきめる
#result = math.gcd(x, y)
#これでも可能
def gcd(a, b):
    while b != 0:
        a, b = b, a % b #aをbに、bをa % bにループさせていく
    return a
#whileのループが終わった後に戻り値を出す
a = 10
b = 20
result = gcd(a, b)
print(f"{a}と{b}の最小公倍数は{result}です")   

a = 14
b = 91
result = gcd(a, b)
print(f"{a}と{b}の最小公倍数は{result}です")

a = 91
b = 14
result = gcd(a, b)
print(f"{a}と{b}の最小公倍数は{result}です")