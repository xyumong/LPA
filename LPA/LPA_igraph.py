# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:23:54 2018

@author: mengxiaoyu
"""

f = open('D:\算法\LPA\LPAdataset.txt','r')
test = {}
for i in f.readlines()[1:]:
    people,friends = i.split(' ')[0],i.split(',')[1:] #根据自己数据集去索引相应内容
    test.setdefault(people,friends) 

import igraph
g = igraph.Graph()
for i in test.keys():
    g.add_vertices(str(i))
edges = []
for i in test.keys():
    for j in test[i]:
        edges.append((str(i),str(j)))
#去重
new = []
for i in edges:
    new.append(tuple(sorted(list(i))))

g.add_edges(set(new))

print (g.community_label_propagation())
igraph.plot(g)
