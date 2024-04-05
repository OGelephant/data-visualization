import matplotlib.pyplot as ply
# 解决中文显示问题
ply.rcParams['font.sans-serif'] = ['SimHei']
ply.rcParams['axes.unicode_minus'] = False

x_values = list(range(1,1001))
y_values = [i**2 for i in x_values]

ply.scatter(x_values,y_values,c=y_values,cmap=ply.cm.Blues,edgecolors='none',s=40)


#设置图标标题，并给坐标加上标签
ply.title("平方点",fontsize = 24)
ply.xlabel("值",fontsize = 14)
ply.ylabel("平方",fontsize = 14)


#设置每个坐标轴的取值范围
ply.axis([0,1100,0,1100000])
#标记刻度大小
ply.tick_params(axis="both",which = "major",labelsize = 14)
# ply.show()
#自动保存图表
ply.savefig('square_plot.png',bbox_inches='tight')

