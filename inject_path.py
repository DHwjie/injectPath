import os
from os import listdir
import numpy as np


# 获取轨迹数据文件中txt文件的的文件名，构成列表
truck_file_list = listdir('truck')
# print(type(truck_file_list))
# 列表长度
print(len(truck_file_list))
total_num_truckfile = len(truck_file_list)
#truck_file_list=sorted([int(i.split('.')[0]) for i in truck_temp_list ])
# 列表内容显示
print(truck_file_list)

data_temp = [total_num_truckfile]
l1=[]
# test = np.zeros((m, n), dtype=np.int
data=np.zeros((total_num_truckfile,1000))
print(data_temp)
for i in range (total_num_truckfile):
    file_name = os.getcwd() + '\\truck\\' + truck_file_list[i]
    #print(file_name)
    with open(file_name, mode='r', encoding='utf-8') as f:
        data_temp = f.readlines()
        for j in range(len(data_temp)):
            #data[i][j]=data_temp[j].rstrip("\n").strip(',')
            l1.append(data_temp[j].rstrip("\n").split(','))

print(len(l1))
