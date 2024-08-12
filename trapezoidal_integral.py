from math import sin, pi
#fromを使ってpiとsinを定義する
#import mathとpi、sinを使うとき、math.pi、math.sinとしてもいい
# --example--
# print(sin(0))
# >>> 0
# -----------

a = 0
b = pi / 2
N = 100
h = (b - a) / N

S = 0
#S=0で初期化
for k in range(1, N+1):
    S += sin(a + (k-1) * h) + sin(a + k * h)
#for文の性質を使って繰り返し足していく
S *= h / 2
print(S)

print("これ以前が制御構文の確認問題の解答")
#関数の確認問題
print("これ以降が関数の確認問題の解答")
import numpy as np
def trapezoidal_integration(f, a=0, b=1, n=100):
    x = np. linspace(a, b, n+1)
    #np.linspaceで区間[a,b]をn等分するn+1個の点xを生成
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

# (1) sin(x) の積分
result1 = trapezoidal_integration(np.sin, a=0, b=np.pi/2, n=50)
print(f"Result 1: {result1}")

# (2) 4 / (1 + x^2) の積分
result2 = trapezoidal_integration(lambda x: 4 / (1 + x**2), a=0, b=1, n=100)
print(f"Result 2: {result2}")

# (3) sqrt(pi) * exp(-x^2) の積分
result3 = trapezoidal_integration(lambda x: np.sqrt(np.pi) * np.exp(-x**2), a=-100, b=100, n=1000)
print(f"Result 3: {result3}")
