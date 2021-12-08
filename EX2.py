import random

def fun01(f, n):
    k = 0
    for i in range(0, n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if y <= f(x):
            k += 1
    return k / n


def Pi(x):
    return (1 - x ** 2) ** 0.5


if __name__ == '__main__':
    while True:
        lst = [100, 1000, 10000, 100000, 1000000, 10000000, -1]
        for n in lst:
            if n == -1:
                break
            print("n: %d\t 精度：%f"% (n, 4 * fun01(Pi, n)))
        break
