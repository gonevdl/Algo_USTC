import random
while True:
    n = int(input("输入精度："))
    if n == -1:
        break
    k = 0
    for i in range(0, n):
        x = random.uniform(0, 1)
        # y = random.uniform(0, 1)
        y = x
        if (x ** 2 + y ** 2) <= 1:
            k += 1
    print(4 * k / n)


if __name__ == "__main__":
    pass
