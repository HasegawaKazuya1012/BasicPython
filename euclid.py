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

print("これ以前が制御構文の確認問題の解答")
#関数の確認問題
print("これ以降が関数の確認問題の解答")
print("問三")
def gcd(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a
#-> intを追加しただけ
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

print("問四")

def coprime(a, b) -> bool:
    return gcd(a, b) == 1

print("エクストラ")
import random

def estimate_coprime_probability(trials: int) -> float:
    coprime_count = 0
    for _ in range(trials):
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        if coprime(a, b):
            coprime_count += 1
    return coprime_count / trials

# 試行回数を10万回とする
probability = estimate_coprime_probability(100000)
print(f"互いに素である確率: {probability}")
