def find_least_soldier(n_k, k, dick):
    # 先判断是否满足组成k个纯职业小组
    team_number = 0
    for val in dick.values():
        team_number+=val//3
    if team_number<k:
        return -1
    # 满足
    people_number=0 
    count=0
    y=k 
    #遍历每个职业对应的人数，这里的思想大概是找到*最多*多少士兵满足k-1个纯职业小组，然后在这个人数基础上加1得到*至少*需要多少士兵可以组成k个纯职业小组
    #因为前面已经判断了是否满足组成k个纯职业小组，所以这个条件一定成立
    for val in dick.values(): 
        # 对应找最多多少士兵满足 0 个纯职业小组
        if y == 1: 
            if val >= 3:
                people_number += 2
            else:
                people_number += val
        # val//3>=y 表明遍历到这里已经能满足k-1个职业小组了。后续找最多多少士兵满足 0 个纯职业小组，所以令y == 1 
        elif val // 3 >= y: 
            people_number += 3 * (y - 1) + 2
            y = 1 
        # 对应目前遍历到的val不满足 k-1 个职业小组，分情况讨论
        else:
            # val % 3 == 2 余2满足最多士兵的思想，人数直接加就行
            if val % 3 == 2:
                people_number += val
                y -= val // 3
            # val % 3 == 1 余1不满足最多士兵的思想，但（val-2）%3==2，并且用count记录这里有一次操作 
            elif val % 3 == 1:
                people_number += val - 2
                y -= val // 3 - 1
                count += 1
            # 同上（val-1）% 3==2
            else:
                people_number += val - 1
                y -= val // 3 - 1
    # 在计算y的时候我们多了一个减1的操作，因此可能会出现 y!= 1
    if y != 1:
        # 如果count>=y-1说明val%3==1所对应的val值能满足找最多士兵的思想，所以把缺少的人数加上就行了。
        if count >= y - 1:
            people_number += 2 * (y - 1)
        else:
            # 这里把所有的val%3==1缺少的人数都加上了人还不够，所以再把val%3==0里缺少的人再加上
            people_number += 2 * count + y - 1 - count
    return people_number + 1
T = int(input())
results = []
for _ in range(T):
    dick = {} 
    n_t ,k = map(int, input().split())
    for _ in range(n_t):
        a_i, b_i = map(int, input().split())
        dick[a_i] = b_i
    dick = dict(sorted(dick.items(), key=lambda x: x[1], reverse=True)) ###
    results.append(find_least_soldier(n_t, k, dick))
for result in results:
    print(result)