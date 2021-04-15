#  coding ='utf-8'
import os
from os import listdir


def read_data():
    truck_file_list = listdir('truck')
    # 列表内容显示
    # print(truck_file_list)
    total_num_truckfile = len(truck_file_list)
    data = [[] for _ in range(total_num_truckfile)]

    for i in range(total_num_truckfile):
        file_name = os.getcwd() + '\\truck\\' + truck_file_list[i]
        # 测试输出filename
        # print(file_name)
        with open(file_name, mode='r', encoding='utf-8') as f:
            data_temp = f.readlines()
            for j in range(len(data_temp)):
                # data[i][j]=data_temp[j].rstrip("\n").strip(',')
                data[i].append(data_temp[j].rstrip("\n").split(','))

    for i in range(total_num_truckfile):
        for j in range(len(data[i])):
            data[i][j] = list(map(eval, data[i][j]))

    # 将data数据按序号（第一个值）排序
    data.sort(key=lambda x: x[0])
    # 测试数据内容输出
    # print(data)
    return data


def inject():
    path_data = read_data()
    print(path_data[0][0])


if __name__ == '__main__':
    inject()
