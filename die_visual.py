from die import Die
import pygal

#创建一个D6
die = Die()
die_2=Die()

#掷色子，并把结果存储在列表中
results = []
for roll_num in range(1000):
    result = die.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies=[]
max_result = die.num_sides+die_2.num_sides

for value in range(1,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "运行1000次"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "结果"
hist.y_title = "频率结果"
hist.add('D6+D6',frequencies)
hist.render_to_file("die_visual.svg")
