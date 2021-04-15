#  coding ='utf-8'
import os
from os import listdir
import copy


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
    inject_distance = 0.00012
    # 初始化已携带病毒传染源列表（含初始传染源），并置空
    inject_total_data = []
    # 初始化被感染的传染源列表（不含初始传染源），并置空
    inject_data = []
    inject_total_data.append(path_data[first_num][0])
    print(inject_total_data)
    count = 0
    for i in range(len(path_data)):
        for j in range(1, min(len(path_data[i]) - 1, len(path_data[first_num])) - 1):
            """
                增加三个时间节点内的距离判断（前后各一个），调整循化范围，使得从第二个时间点开始判断到倒数第二个时间点，
                然后算三个时间点内的距离，如果最大的时间节点的位置都可以满足要求，其前后各个时间点位置的也都可以满足时距离要求
                此时保存最先的那个点即可
            """
            temp_distance_x1 = (path_data[i][j - 1][2] - path_data[first_num][j - 1][2]) ** 2
            temp_distance_y1 = (path_data[i][j - 1][3] - path_data[first_num][j - 1][3]) ** 2
            temp_distance1 = (temp_distance_x1 + temp_distance_y1) ** 0.5
            temp_distance_x2 = (path_data[i][j][2] - path_data[first_num][j][2]) ** 2
            temp_distance_y2 = (path_data[i][j][3] - path_data[first_num][j][3]) ** 2
            temp_distance2 = (temp_distance_x2 + temp_distance_y2) ** 0.5
            temp_distance_x3 = (path_data[i][j + 1][2] - path_data[first_num][j + 1][2]) ** 2
            temp_distance_y3 = (path_data[i][j + 1][3] - path_data[first_num][j + 1][3]) ** 2
            temp_distance3 = (temp_distance_x3 + temp_distance_y3) ** 0.5
            temp_distance = max(temp_distance1, temp_distance2, temp_distance3)
            if (temp_distance <= inject_distance) & (temp_distance != 0.0):
                print(path_data[i][j][0], '号与', path_data[first_num][j][0], '号，在时间点：', path_data[i][j][1],
                      '处发生传染行为，传染距离为：', temp_distance)
                count = count + 1
                inject_total_data.append(path_data[i][j])
                # 此处加判断潜伏期内容，判读时间点加delay_time后是否还在即可，如果不在，就直接去掉了
                if (path_data[i][j][1] + delay_time) < (len(path_data[i]) - 1):
                    inject_data.append(path_data[i][j])
                else:
                    break
                break
    # print(inject_total_data)
    # print(inject_data)

    while (True):
        flag_len = 0
        count = len(inject_data)
        temp_len = count
        for i in range(len(inject_data)):
            # print('传染源数据：', inject_data[i])
            # 传染源数据的编号
            flag_num = inject_data[i][0] - 1
            # 传染源被感染时间
            flag_inject_time = inject_data[i][1]
            for i2 in range(len(path_data)):
                if (len(path_data[i2]) > flag_inject_time):
                    for j2 in range(flag_inject_time + delay_time,
                                    min(len(path_data[flag_num]), len(path_data[i2]) - 1) - 1):
                        # 欧式距离 和我们中学所学的（x1,y1），（x2,y2）计算的距离一样 根号下[（x1-x2）²+(y1-y2)²]
                        # temp_distance = (((path_data[i2][j2][2] - path_data[flag_num][j2][2]) ** 2) + (
                        #     (path_data[i2][j2][3] - path_data[flag_num][j2][3])) ** 2) ** 0.5
                        temp_distance_x1 = (path_data[i2][j2 - 1][2] - path_data[flag_num][j2 - 1][2]) ** 2
                        temp_distance_y1 = (path_data[i2][j2 - 1][3] - path_data[flag_num][j2 - 1][3]) ** 2
                        temp_distance1 = (temp_distance_x1 + temp_distance_y1) ** 0.5
                        temp_distance_x2 = (path_data[i2][j2][2] - path_data[flag_num][j2][2]) ** 2
                        temp_distance_y2 = (path_data[i2][j2][3] - path_data[flag_num][j2][3]) ** 2
                        temp_distance2 = (temp_distance_x2 + temp_distance_y2) ** 0.5
                        temp_distance_x3 = (path_data[i2][j2 + 1][2] - path_data[flag_num][j2 + 1][2]) ** 2
                        temp_distance_y3 = (path_data[i2][j2 + 1][3] - path_data[flag_num][j2 + 1][3]) ** 2
                        temp_distance3 = (temp_distance_x3 + temp_distance_y3) ** 0.5
                        temp_distance = max(temp_distance1, temp_distance2, temp_distance3)
                        # print(path_data[i2][j2], '与', path_data[flag_num][j2], '的距离为：', temp_distance)
                        if (temp_distance <= inject_distance) & (temp_distance != 0.0):
                            # print(path_data[i2][j2], '与', path_data[flag_num][j2], '的距离为：', temp_distance)
                            print(path_data[i2][j2][0], '号与', path_data[flag_num][j2][0], '号，在时间点：',
                                  path_data[i2][j2][1],
                                  '处发生传染行为，传染距离为：', temp_distance)
                            inject_total_data.append(path_data[i2][j2])
                            # 去重
                            dic = list(set([tuple(t) for t in inject_total_data]))
                            inject_total_data = [list(v) for v in dic]
                            inject_total_data.sort(key=lambda x: [x[0], x[1]])
                            if (path_data[i2][j2][1] + delay_time) < (len(path_data[i2]) - 1):
                                inject_data.append(path_data[i2][j2])
                                # 去重
                                dic = list(set([tuple(t) for t in inject_data]))
                                inject_data = [list(v) for v in dic]
                                inject_data.sort(key=lambda x: [x[0], x[1]])
                            else:
                                break
                            # print('传染源数据列表：',inject_data)
                            print('传染源数据列表长度：', len(inject_data))
                            flag_len = temp_len - len(inject_data)
                else:
                    # print(path_data[i2][0],'一共',len(path_data[i2]),'行,i_t=',flag_inject_time)
                    break
        if flag_len == 0:
            break
    # print('全部：', inject_total_data)
    # print(len(inject_total_data))
    # print('除去初始传染源：', inject_data)
    # print(len(inject_data))
    return inject_total_data


def setData(injectdata):
    li = []
    li.append(injectdata[0])
    for i in range(1, len(injectdata) - 1):
        if injectdata[i][0] != injectdata[i - 1][0]:
            li.append(injectdata[i])
        else:
            continue

    return li


def inject():
    path_data = readData()
    # print(len(path_data))
    # print(path_data[0][0])
    init_num = int(input('请输入初始传染源标号(1-276)：').strip())
    # print(init_num)
    # print(type(init_num))
    injectData = injectCheck(path_data, init_num)
    injectData = setData(injectData)
    print(injectData)
    print('共计感染{}人！'.format(len(injectData)))
    # for num in injectData:
    print('编号分别为：', *[num[0] for num in injectData])


if __name__ == '__main__':
    inject()
