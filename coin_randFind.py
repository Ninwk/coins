from numpy import random
import coin_compare as c


def find(num):
    """

    :param num:要寻找假币的次数
    :return:
    """

    while num:
        # 硬币列表 先定义为空列表

        coin = []

        # 硬币的总数量
        tot_Num = random.randint(3, 20)
        # 假币的位置
        fa_Numb = random.randint(0, tot_Num - 1)
        # 硬币重量
        co_weight = random.randint(1, 10)
        # 假币重量
        fco_weight = random.randint(1, 10)
        while fco_weight is co_weight:
            fco_weight = random.randint(1, 10)

        # 添加硬币重量至硬币列表
        for i in range(tot_Num):
            coin.append(co_weight)

        # 插入假币
        coin[fa_Numb] = fco_weight
        print("本次为第%d次生成硬币列表,硬币数量为%d个" % (abs(4-num), tot_Num))

        print(coin)
        num_co = c.compare_coin(coin, 0, tot_Num - 1)

        print("找到了假币位置下标为%d "%num_co)
        print("————————————————————————————————————————————————————————————————————————————————————————————————")
        print()
        # 打印硬币列表
        num = num - 1


def pri_name():
    print("————————————————————————————————————————————————————————————————————————————————————————————————")
    print("查找假币，假币只有一颗，不知道位置，不知道轻重，随机生成硬币数量与假币位置，")
    my_idna = 18401010124
    my_chas = "网络181"
    my_name = "吴冰寒"
    print("学号:%d,班级:%s,姓名:%s" % (my_idna, my_chas, my_name))
