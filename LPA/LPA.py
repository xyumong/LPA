# -*- coding: utf-8 -*-
"""
Spyder Editor

LPA（标签传播算法）.
1>为每个节点随机指定一个自己特有的标签
2>逐轮刷新所有节点的标签，直到所有节点的标签不再发生变化为止
  --考察邻居节点的标签，将出现个数最多的那个标签赋值给当前节点，当个数最多的标签不唯一时，
    随机选择一个标签赋值给当前节点
    
  --同步更新：节点x在t时刻的更新是基于邻居节点在t-1时刻的标签
  --异步更新：节点x在t时刻的更新时，其部分邻居节点是t时刻更新的标签，还有部分邻居节点是t-1时刻更新的标签

author：mengxiaoyu

date：2018/7/10
"""



def loadLpaData(filename):
    f = open(filename,'r')
    data = {}
    for i in f.readlines():
        i=i.strip()
        order,ship = i.split(' ')[0],i.split(' ')[-1]
        ships = ship.split(',')
        data.setdefault(order,ships)
    f.close()
    return data

def getMost(ships):
    #获取数目最多的相邻节点，有多个的话随机选一个
    import collections
    counter = collections.Counter(ships)
    tmp = sorted(counter.items(),key = lambda x:x[1])
    
    maxc = tmp[-1][1]
    maxset = []
    for i in tmp:
        if i[1] == maxc:maxset.append(i[0])
    
    import random
    random.shuffle(maxset)
    return maxset[0]
def updateShips(cluster,data):
    #更新标签
    for _ in data.keys():
        data[_] = [cluster[i] for i in data[_]]
def checkStatus(cluster,data):
    #检查是否收敛
    flag = 0
    for d in data.keys():
        if cluster[d] != getMost(data[d]):return 0
    return 1
def main(mydata):
    #主函数
    data = mydata.copy()
    cluster = dict([(_,_) for _ in data.keys()])
    while 1:
        if checkStatus(cluster,data):break
        for i in cluster.keys():
            cluster[i] = getMost(data[i])
            updateShips(cluster,data)
    return cluster

data = loadLpaData(r'D:\算法\LPA\LPAdataset.txt')
main(data)


