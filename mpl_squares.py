import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5)

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#设置图标标题，并给坐标轴加上标签
plt.title("值和平方",fontsize = 24)
plt.xlabel("值",fontsize = 14)
plt.ylabel("值的平方",fontsize = 14)

#设置刻度大小
plt.tick_params(axis="both",labelsize = 14)
plt.show()