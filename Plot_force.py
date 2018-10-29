from Data_Struct import *
from Fmx_Calculate import *
from Equation_Of_State import * 
import matplotlib.pyplot as plt
from Project_Parameters import *
import numpy as np
#import matplotlib.animation as animation
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False 
Lr_seq = range(40 , 500, 20)

wind_seq = []
low_temp_seq = []
high_temp_seq = []
ice_seq = []
ave_seq = []
construc_seq = []
check_seq = []
for Lr in Lr_seq:
	control_condition = find_control_condition(Lr, True)
	#print(control_condition)
	if (control_condition == '年平'):
		sigma_control = cond.sigma_av 
	else:
		sigma_control = cond.sigma_max
	#control_condition = '年平'
	print('{}m档距下控制工况:\n'.format(Lr),control_condition, sigma_control)

	high_temp_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['高温'])*cond.area/1000)
	low_temp_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['低温'])*cond.area/1000)
	wind_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['大风'])*cond.area/1000)
	ice_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['覆冰'])*cond.area/1000)
	ave_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['年平'])*cond.area/1000)
	construc_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['安装'])*cond.area/1000)
	check_seq.append(sol_equation_of_state(Lr, cond, \
		weather_dict[control_condition],weather_dict['验算'])*cond.area/1000)

plt.plot(Lr_seq,high_temp_seq, color = 'red' , label = '高温', linestyle = '--', linewidth = 3)
plt.plot(Lr_seq,low_temp_seq, color = 'green', label = '低温', linestyle = '--', linewidth = 3)
plt.plot(Lr_seq,ice_seq, color = 'black' , label = '覆冰', linestyle = '--', linewidth = 3)
plt.plot(Lr_seq,ave_seq, color = 'blue' , label = '年平', linestyle = '--', linewidth = 3)
plt.axhline(y = cond.Tav/1000, color = 'black' , label = '年平限值', linestyle = '-', linewidth = 1)
plt.axhline(y = cond.Tmax/1000, color = 'red' , label = '设计限值', linestyle = '-', linewidth = 1)
plt.xlabel('档距 m ')
plt.ylabel('拉力 kN')
plt.xlim(min(Lr_seq),max(Lr_seq)+200)
#plt.plot(Lr_seq,construc_seq, color = 'c' , label = '安装')
#plt.plot(Lr_seq,ave_seq, color = 'yellow' , label = '验算')
plt.legend()
plt.show()
'''
Lr_seq=np.arange(40,400,20)
fig, ax  = plt.subplots()
xdata, ydata = [], []
l1, = ax.plot([],[],'r-')
l2, = ax.plot([],[],'r-')
l3, = ax.plot([],[],'r-')
l4, = ax.plot([],[],'r-')
#control_condition = find_control_condition(Lr, True)	
control_condition = '年平'
	#print(control_condition)
if (control_condition == '年平'):
	sigma_control = cond.sigma_av 
else:
	sigma_control = cond.sigma_max
def init():
	ax.set_xlim(0,400)
	return l1,	
def animate(i):
	l1.set_ydata(sol_equation_of_state(i, cond, weather_dict[control_condition],weather_dict['高温'])*cond.area/1000)
	#l2.set_ydata(sol_equation_of_state(i, cond, weather_dict[control_condition],weather_dict['大风'])*cond.area/1000)
	return l1,

ani = animation.FuncAnimation(fig, animate, Lr_seq, init_func=init, interval = 25, blit=False)
plt.show()
'''