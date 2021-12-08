import random
import numpy as np

MIN_NUM = -9999999999999
count = 0

# 函数找出给定数组对应的p[]
def findP(val: list[int]):
    head = 0
    P = [MIN_NUM] + [0] * (len(val) - 1)
    val_pos = [[MIN_NUM, 0]]
    for i in range(1, len(val)):
        val_pos.append([val[i], i])
    val_pos.sort()
    max = val_pos[-1][0]
    head = val_pos[1][1]
    # print(max)
    for i in range(1, len(val)):
        if val[i] != max:
            pos = 0
            for j in range(1, len(val)):
                if val_pos[j][0] == val[i]:
                    if j != (len(val) - 1):
                        pos = val_pos[j + 1][1]
                    else:
                        pos = 0
                    break
            P[i] = pos
        else:
            P[i] = 0
    return P, head


def Search(x: int, i: int, val: list[int], P: list[int]):
    global count
    while x > val[i]:
        count += 1
        i = P[i]
    return i, count


def SearchD(x: int, head: int, val: list[int], P: list[int]):
    # i = random.randint(1, 10000)
    i = 1
    y = val[i]

    if x < y:
        return Search(x, head, val, P)
    elif x > y:
        return Search(x, P[i], val, P)
    else:
        return i, 1


def SearchB(x: int, head: int, val: list[int], P: list[int]):
    i = head
    max = val[i]
    global count
    for j in range(1, int(np.sqrt(len(val))) + 1):
        count += 1
        y = val[j]
        if max < y <= x:
            i = j
            max = y

    return Search(x, i, val, P)


if __name__ == '__main__':

    # count_lst_A = []
    # for i in range(0, 10):
    #     val = [MIN_NUM] + random.sample(range(0, 10000), 10000)
    #     # print(val)
    #     P, head = findP(val)
    #     count_lst_A.append(Search(random.randint(0, 9999), head, val, P)[1])
    #     # print(count_lst)
    # cnt_lst_A = np.array(count_lst_A)

    #     """count_lst_D = []
    #     for i in range(0, 10):
    #         val = [MIN_NUM] + random.sample(range(0, 10000), 10000)
    #         P, head = findP(val)
    #         print(val)
    #         # count_lst_B.append(SearchD(random.randint(0, 9999), head, val, P)[1])
    #         count_lst_D.append(SearchD(random.randint(0, 9999), head, val, P)[1])
    #     cnt_lst_D = np.array(count_lst_D)
    #     print(cnt_lst_D)
    #     print(np.mean(cnt_lst_D))
    #     print(np.min(cnt_lst_D))
    # """

    count_lst_B = []
    for i in range(0, 1000):
        count = 0
        val = [MIN_NUM] + [i for i in range(0, 10000)]
        # print(val)
        P, head = findP(val)
        _, _ = SearchB(random.randint(0, 9999), head, val, P)
        count_lst_B.append(count)
        print("第%d轮" % i, count_lst_B)
    cnt_lst_B = np.array(count_lst_B)
    print(cnt_lst_B)
    print(np.average(cnt_lst_B))
    print(np.min(cnt_lst_B))
    print(np.max(cnt_lst_B))


