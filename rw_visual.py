import matplotlib.pyplot as plt
from random_walk import RandomWalk

#只要处于活动状态，就不断的模拟随机漫步
while True:
    #创建一个RandomWalk实例。并将点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    #设置窗口的尺寸
    plt.figure(dpi=80,figsize=(10,6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)

    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)

    #隐藏坐标轴
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(labelbottom=False, labelleft=False, length=0)

    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break