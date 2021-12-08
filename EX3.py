import random


# 定义的通用积分函数
def integration(a, b, c, d, n, f):
    k = 0
    for i in range(0, n):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        if y <= f(x):
            k += 1
    return (b - a) * (d - c) * k / n


if __name__ == '__main__':

    # 要积分的函数
    def fun(x):
        return x ** 2


    # n的精度
    lst = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    # 各个参数的值
    a, b, c, d, = 2, 3, 0, 10
    # 打印结果
    for n in lst:
        print("[a, b]: [%d, %d]\t[c, d]: [%d, %d]\tn: %d\t精度：%f" % (a, b, c, d, n, integration(a, b, c, d, n, fun)))
