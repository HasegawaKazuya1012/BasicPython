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