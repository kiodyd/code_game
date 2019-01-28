import copy

maps = list()
existent_list = list()
build_list = list()
is_start = True
find_target = False

# 初始化地图的程序
def map_init(h,w):
    temps = list()   
    for i in range(0,w):
        temp = [x*0 for x in range(0,h)]
        temps.append(temp)
    return temps

# 判断某个点是否合法  （出界  或者有值）
def legal_pos(x,y,h,w):
    if x < w and y < h and x>=0 and y>=0:
        return True if maps[x][y] == 0 else False
    else:
        return False

# 用于判断两个door之间是否可通的一个列表
def in_exist_list(x,y):
    return (x,y) in existent_list

#判断两个door之间是否可以联通  利用递归
def door_to_door(sx,sy,ex,ey,h,w):
    global is_start
    global find_target
    if sx == ex and sy == ey:
        find_target = True
        return
    if not legal_pos(sx,sy,h,w) and not is_start:
        return
    elif legal_pos(sx,sy,h,w) and not is_start:
        existent_list.append((sx,sy))
    is_start = False
    if (not in_exist_list(sx+1,sy)):
        door_to_door(sx+1,sy,ex,ey,h,w)
    if (not in_exist_list(sx-1,sy)):
        door_to_door(sx-1,sy,ex,ey,h,w)
    if (not in_exist_list(sx,sy+1)):
        door_to_door(sx,sy+1,ex,ey,h,w)
    if (not in_exist_list(sx,sy-1)):
        door_to_door(sx,sy-1,ex,ey,h,w)
    

# 主要思路是先把第一个建筑物可以放的位置先记录下来  然后接下来的建筑物在第一个建筑物的基础上实施  判断是否合法
data = list(map(lambda x : eval(x),input().split()))
maps = map_init(data[0],data[1])
temp_maps = list()
temp_door = list()
first_build = True
for i in range(0,data[2]):
    build = (list(map(lambda x : eval(x),input().split())))
    map_i = list()
    door_i = list()
    if first_build:
        first_build = False
        for ii in range(0,data[0]-build[0]+1):
            for jj in range(0,data[1]-build[1]+1):
                door = (jj + build[3] - 1,ii + build[2] - 1)
                door_i.append(door)
                temp = map_init(data[0],data[1])
                for iii in range(0,build[0]):
                    for jjj in range(0,build[1]):
                        temp[jj + jjj][ii + iii] = i+1
                map_i.append(temp)
    else:
        for map_index in range(0,len(temp_maps[i-1])):
            for ii in range(0,data[0]-build[0]+1):
                for jj in range(0,data[1]-build[1]+1):
                    maps = temp_maps[i-1][map_index]
                    break_flag = False
                    temp = copy.deepcopy(maps) #深度复制
                    for iii in range(0,build[0]):
                        for jjj in range(0,build[1]):
                            if(legal_pos(jj + jjj,ii + iii,data[0],data[1])):
                                temp[jj + jjj][ii + iii] = i+1
                            else:
                                break_flag = True
                                break
                        if break_flag:
                            break
                    if break_flag:
                        continue
                    door = (jj + build[3] - 1,ii + build[2] - 1)

                    is_start = True
                    find_target = False
                    maps = temp
                    door_to_door(door[0],door[1],temp_door[i-1][map_index][0],temp_door[i-1][map_index][1],data[0],data[1])
                    if not find_target:
                        continue

                    map_i.append(temp)
                    door_i.append(door)

    temp_maps.append(map_i)
    temp_door.append(door_i)

    
#用于转换坐标（xy反转  一开始想列表首层表示x第二层表示y  但后面发现有问题  有时间的话需要重构）和筛选合适的地图   
for i in range(len(temp_maps)):
    if temp_maps[len(temp_maps) - i -1] != []:
        new_map = map_init(data[1],data[0])
        if(len(temp_maps[len(temp_maps) - i -1]) == 1):
            for ii in range(0,data[1]):
                for jj in range(0,data[0]):
                    new_map[jj][ii] = temp_maps[len(temp_maps) - i -1][0][ii][jj]
        else:
            index = -1
            new_maps = []    #输出转换坐标后的地图集合
            border_times = []   #改地图碰到边界的次数    尽可能让地图处于中间
            for temp_map in temp_maps[len(temp_maps) - i -1]:
                index = index + 1
                border = [0,0,0,0]   #分别是上右下左边界  0代表没碰到
                for ii in range(0,data[1]):
                    for jj in range(0,data[0]):
                        new_map[jj][ii] = temp_map[ii][jj]
                        if (new_map[jj][0] != 0):
                            border[0] = 1
                        if (new_map[data[0]-1][ii] != 0):
                            border[1] = 1
                        if (new_map[jj][data[1] - 1] != 0):
                            border[2] = 1
                        if (new_map[0][ii] != 0):
                            border[3] = 1

                border_times.append(border)
                new_maps.append(copy.deepcopy(new_map))
            
            min_time = (0,5)  #[0]是index  [1]是次数
            for i in range(len(border_times)):
                time = border_times[i][0] + border_times[i][1] + border_times[i][2] + border_times[i][3]
                if time < min_time[1]:
                    min_time = (i,time)
            new_map = new_maps[min_time[0]]

        for line in new_map:
            print(" ".join(list(map(lambda x : str(x),line))))
        break
