a = 61
b = 10

# TODO
if a <= 1:
    print("aは素数ではありません")
else:
    for i in range(2 , int(a**0.5) + 1):
        if a % i == 0:
            print("aは素数ではありません")
            break
        else:
            print("aは素数です")
            break

if b <= 1:
    print("bは素数ではありません")
else:
    for i in range(2 , int(b**0.5)+1):
        if b % i == 0:
            print("bは素数ではありません")
            break
        else:
                print("bは素数です")
                break

#関数の確認問題
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = 61
b = 10

if prime(a):
    print(f"{a}は素数です")
else:
    print(f"{a}は素数ではありません")

if prime(b):
    print(f"{b}は素数です")
else:
    print(f"{b}は素数ではありません")
