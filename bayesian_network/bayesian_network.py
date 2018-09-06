# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:05:34 2018

@author: mengxiaoyu
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# 通过边来定义贝叶斯模型
model = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# 定义条件概率分布
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6, 0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7, 0.3]])

# variable：变量
# variable_card：基数
# values：变量值
# evidence：
cpd_g = TabularCPD(variable='G', variable_card=3, 
                   values=[[0.3, 0.05, 0.9,  0.5],
                           [0.4, 0.25, 0.08, 0.3],
                           [0.3, 0.7,  0.02, 0.2]],
                  evidence=['I', 'D'],
                  evidence_card=[2, 2])

cpd_l = TabularCPD(variable='L', variable_card=2, 
                   values=[[0.1, 0.4, 0.99],
                           [0.9, 0.6, 0.01]],
                   evidence=['G'],
                   evidence_card=[3])

cpd_s = TabularCPD(variable='S', variable_card=2,
                   values=[[0.95, 0.2],
                           [0.05, 0.8]],
                   evidence=['I'],
                   evidence_card=[2])

# 将有向无环图与条件概率分布表关联
model.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# 验证模型：检查网络结构和CPD，并验证CPD是否正确定义和总和为1
model.check_model()
