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

path_data = [[] for i in range(276)]

# print(path_data)

# 遍历文件，将轨迹信息读入path_data[]列表中
for i in range(total_num_truckfile):
    file_name = os.getcwd() + '\\truck\\' + truck_file_list[i]
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

# 测试输出
print(path_data[0][0])  # 输出：[1, 1, 23.845089, 38.01847]
print(len(path_data[0]))  # 输出：45

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
inject_data = []
temp_distance = 0.0
inject_range = 0.00002
count = 0
# 取flag对应值为初始传染源
for i in range(total_num_truckfile):
    for j in range(len(path_data[i])):
        # path_data[i][j] = list(map(eval, path_data[i][j]))
        temp_distance = (((path_data[i][j][2] - path_data[flag][j][2]) ** 2) + ((path_data[i][j][3] - path_data[flag][j][3])) ** 2) ** 0.5
        # data_distance.append((((path_data[i][j][2]-path_data[flag][j][2])**2)+((path_data[i][j][3]-path_data[flag][j][3]))**2)**0.5)
        # print(path_data[i][j], '与', path_data[flag][j], '的距离为：', temp_distance)
        if (temp_distance <= inject_range) & (temp_distance != 0.0):
            print(path_data[i][j], '与', path_data[flag][j], '的距离为：', temp_distance)
            count = count + 1
            inject_data.append(path_data[i][j])
            break;
print(count)
print(inject_data)

inject_temp = []
for i in range(len(inject_data)):
    print(inject_data[i])
    flag_num = inject_data[i][0]
    print(flag_num)
    flag_inject_time = inject_data[i][1]
    print(flag_inject_time)
    for i2 in range(total_num_truckfile):
        for j2 in range(len(path_data[i2])):
            if (len(path_data[i2])>flag_inject_time):
                pass
            else:
                print(path_data[i2][0],'一共',len(path_data[i2]),'行,i_t=',flag_inject_time)
                break


