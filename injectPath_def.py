#  coding ='utf-8'
import os
from os import listdir


def readData():
    """
    功能：实现truck数据的读入与格式化排序，以满足后续使用
    参数：无
    返回值：data
    其它介绍：将truck里的数据导入，并对其数据格式化排序(增序)
            格式化后的数据实例：[1, 1, 23.845089, 38.01847]
    """
    # 读取truck文件中文件名，truck_file_list用于保存
    truck_file_list = listdir('truck')
    # 列表内容显示
    # print(truck_file_list)
    # 统计truck文件下txt文件数量
    total_num_truckfile = len(truck_file_list)
    # 初始化构建data二维空列表
    data = [[] for _ in range(total_num_truckfile)]

    # 循环打开truck文件夹里的文件，将每个txt文件中的数据导入data中
    for i in range(total_num_truckfile):
        file_name = os.getcwd() + '/truck/' + truck_file_list[i]
        # 测试输出filename路径
        # print(file_name)
        with open(file_name, mode='r', encoding='utf-8') as f:
            # 直接读入（数据量不大使可以使用）
            data_temp = f.readlines()
            for j in range(len(data_temp)):
                # 数据导入格式化（去除导入数据时每一行末尾的换行符和数据之间的','）
                data[i].append(data_temp[j].rstrip("\n").split(','))
    # 数据导入后是字符串形式，通过下面的循环，将数据类型转换为数据本身的类型（int/float）
    for i in range(total_num_truckfile):
        for j in range(len(data[i])):
            data[i][j] = list(map(eval, data[i][j]))

    # 将data数据按序号（第一个值）排序
    data.sort(key=lambda x: x[0])
    # 测试数据内容输出
    # print(data)
    # 将导入并格式化好的数据以多维列表的形式返回
    return data


def injectCheck(data, initnum):
    path_data = data
    # 初始传染源编号
    first_num = initnum - 1
    # 占用时间节点数量来模拟潜伏期
    delay_time = 2
    # 定为接触时间（近距离接触的时间范围）
    range_time = 3
    # 模拟感染距离
    inject_distance = 0.00002
    # 初始化已携带病毒传染源列表（含初始传染源），并置空
    inject_total_data = []
    # 初始化被感染的传染源列表（不含初始传染源），并置空
    inject_data = []
    inject_total_data.append(path_data[first_num][0])
    print(inject_data)
    count = 0
    for i in range(len(path_data)):
        for j in range(min(len(path_data[i]) - 1, len(path_data[first_num]))):
            """
                增加三个时间节点内的距离判断（前后各一个），调整循化范围，使得从第二个时间点开始判断到倒数第二个时间点，然后算三个时间点内的距离，取最大值
                如果最大的时间节点的位置都可以满足要求，其前后各个时间点位置的也都可以满足时距离要求
                此时保存最先的那个点即可
            """
            temp_distance_x = (path_data[i][j][2] - path_data[first_num][j][2]) ** 2
            temp_distance_y = (path_data[i][j][3] - path_data[first_num][j][3]) ** 2
            temp_distance = (temp_distance_x + temp_distance_y) ** 0.5
            if (temp_distance <= inject_distance) & (temp_distance != 0.0):
                print(path_data[i][j], '与', path_data[first_num][j], '的距离为：', temp_distance)
                count = count + 1
                inject_total_data.append(path_data[i][j])
                # 此处加判断潜伏期内容，判读时间点加delay_time后是否还在即可，如果不在，就直接去掉了
                inject_data.append(path_data[i][j])
                break
    print(inject_data)
    # while (True):
    #     temp_len = 0
    #     count = len(inject_distance)
    #     temp_len = count
    #     for i in range(len(inject_data)):
    #         print('传染源数据：', inject_data[i])
    #         # 传染源编号
    #         flag_num = inject_data[i][0] - 1
    #         # 传染源被感染时间
    #         flag_inject_time = inject_data[i][1]


def inject():
    path_data = readData()
    print(len(path_data))
    print(path_data[0][0])
    init_num = int(input('请输入初始传染源标号(0-276)：').strip())
    print(init_num)
    print(type(init_num))
    injectCheck(path_data, init_num)


if __name__ == '__main__':
    inject()
