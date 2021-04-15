import os
from os import listdir
import numpy as np

# 获取轨迹数据文件中txt文件的的文件名，构成列表
truck_file_list = listdir('truck')
# print(type(truck_file_list))
# 列表长度
# print(len(truck_file_list))
total_num_truckfile = len(truck_file_list)
# truck_file_list=sorted([int(i.split('.')[0]) for i in truck_temp_list ])
# 列表内容显示
# print(truck_file_list)

path_data = [[] for i in range(total_num_truckfile)]

# print(path_data)

# 遍历文件，将轨迹信息读入path_data[]列表中
for i in range(total_num_truckfile):
    file_name = os.getcwd() + '/truck/' + truck_file_list[i]
    # print(file_name)
    with open(file_name, mode='r', encoding='utf-8') as f:
        data_temp = f.readlines()
        for j in range(len(data_temp)):
            # data[i][j]=data_temp[j].rstrip("\n").strip(',')
            path_data[i].append(data_temp[j].rstrip("\n").split(','))

# 把列表中字符串类型转换为数值类型（int/float）
for i in range(total_num_truckfile):
    for j in range(len(path_data[i])):
        path_data[i][j] = list(map(eval, path_data[i][j]))

path_data.sort(key=lambda data: data[0])
# 测试输出
print(path_data[0][0])  # 输出：[1, 1, 23.845089, 38.01847]
print(len(path_data[0]))  # 输出：45

# 把时间点最长的数据作为初始传染源
max_len_data = 0
flag = 0
for i in range(total_num_truckfile):
    if len(path_data[i]) != int(path_data[i][len(path_data[i]) - 1][1]):
        print(path_data[i][0])
    # max_len_data=max(max_len_data,len(path_data[i]))
    # print(path_data[i][len(path_data[i])-1][0:2])
    if max_len_data < len(path_data[i]):
        max_len_data = len(path_data[i])
        flag = i
# 测试数据输出
# print(path_data)

print(max_len_data)
inject_data = []  # 用来放被感染的人的信息，后续作为传染源进行多次循环测算距离
temp_distance = 0.0  # 用来放计算后的距离
inject_range = 0.00002  # 多次跑数据测的参数，这个传染距离大概传染17人，太大人数太多，太小人数太少。276个数据，感染17个还算是差不多的。
count = 0
# 取flag对应值为初始传染源
for i in range(total_num_truckfile):
    for j in range(len(path_data[i])):
        # path_data[i][j] = list(map(eval, path_data[i][j]))
        temp_distance = (((path_data[i][j][2] - path_data[flag][j][2]) ** 2) + (
            (path_data[i][j][3] - path_data[flag][j][3])) ** 2) ** 0.5
        # data_distance.append((((path_data[i][j][2]-path_data[flag][j][2])**2)+((path_data[i][j][3]-path_data[flag][j][3]))**2)**0.5)
        # print(path_data[i][j], '与', path_data[flag][j], '的距离为：', temp_distance)
        if (temp_distance <= inject_range) & (temp_distance != 0.0):
            print(path_data[i][j], '与', path_data[flag][j], '的距离为：', temp_distance)
            count = count + 1
            inject_data.append(path_data[i][j])
            break
print(count)
print(inject_data)

# 下面循环判断injec_data列表中的被感染的人能不能传染其他人，如果能，更新injec_data列表后再次判断
count = len(inject_data)
while (True):
    min_len = 0
    count = len(inject_data)
    temp_len = count
    for i in range(len(inject_data)):
        print('被感染的数据：', inject_data[i])
        flag_num = inject_data[i][0] - 1
        print('被感染数据的编号：', flag_num + 1)
        flag_inject_time = inject_data[i][1]
        print('被感染数据的时间点：', flag_inject_time)
        for i2 in range(total_num_truckfile):
            if (len(path_data[i2]) > flag_inject_time):
                for j2 in range(flag_inject_time, min(len(path_data[flag_num]), len(path_data[i2]) - 1)):
                    # 欧式距离 和我们中学所学的（x1,y1），（x2,y2）计算的距离一样 根号下[（x1-x2）²+(y1-y2)²]
                    temp_distance = (((path_data[i2][j2][2] - path_data[flag_num][j2][2]) ** 2) + (
                        (path_data[i2][j2][3] - path_data[flag_num][j2][3])) ** 2) ** 0.5
                    # print(path_data[i2][j2], '与', path_data[flag_num][j2], '的距离为：', temp_distance)
                    if (temp_distance <= inject_range) & (temp_distance != 0.0):
                        print(path_data[i2][j2], '与', path_data[flag_num][j2], '的距离为：', temp_distance)
                        inject_data.append(path_data[i2][j2])
                        # 去重
                        dic = list(set([tuple(t) for t in inject_data]))
                        inject_data = [list(v) for v in dic]
                        inject_data.sort(key=lambda data: data[1])
                        # print(inject_data)
                        min_len = temp_len - len(inject_data)
            else:
                # print(path_data[i2][0],'一共',len(path_data[i2]),'行,i_t=',flag_inject_time)
                break
    if min_len == 0:
        break
inject_data.sort(key=lambda data: data[0])
print(inject_data)
print('共计感染：', len(inject_data), '人。')
