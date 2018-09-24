from Data_Struct import *
from Fmx_Calculate import *
from Wind_Load import *
from Equation_Of_State import *
from Project_Parameters import *
control_condition = find_control_condition(tower.Lr_front)
#print(control_condition)
if (control_condition == '年平'):
	sigma_control = cond.sigma_av
else:
	sigma_control = cond.sigma_max
print('控制工况:\n',control_condition, sigma_control)

print('高温工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['高温'])*cond.area)
print('低温工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['低温'])*cond.area)
print('大风工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['大风'])*cond.area)
print('覆冰工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['覆冰'])*cond.area)
print('年平工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['年平'])*cond.area)
print('安装工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['安装'])*cond.area)
print('验算工况：', sol_equation_of_state(tower.Lr_front, cond, \
	weather_dict[control_condition],weather_dict['验算'])*cond.area)

control_condition = find_control_condition(tower.Lr_back,False)
#print(control_condition)
if (control_condition == '年平'):
	sigma_control = cond.sigma_av
else:
	sigma_control = cond.sigma_max
print('控制工况:\n',control_condition, sigma_control)

print('高温工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['高温'])*cond.area)
print('低温工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['低温'])*cond.area)
print('大风工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['大风'])*cond.area)
print('覆冰工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['覆冰'])*cond.area)
print('年平工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['年平'])*cond.area)
print('安装工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['安装'])*cond.area)
print('验算工况：', sol_equation_of_state(tower.Lr_back, cond, \
	weather_dict[control_condition],weather_dict['验算'])*cond.area)

print('下相导线荷载')
wind_load_conductor=project.split*cal_wind_load_conductor(cond, project.Voltage, wind_max, tower.h_bottom, tower.Lh)
print('线条风荷载:   ',wind_load_conductor)
wind_load_insulator=cal_wind_load_insulator(wind_max, tower.h_bottom, 0.32)
print('绝缘子风荷载: ', wind_load_insulator)

print('中相导线荷载')
wind_load_conductor=project.split*cal_wind_load_conductor(cond, project.Voltage, wind_max, tower.h_medium, tower.Lh)
print('线条风荷载:   ',wind_load_conductor)
wind_load_insulator=cal_wind_load_insulator(wind_max, tower.h_medium, 0.32)
print('绝缘子风荷载: ',wind_load_insulator)

print('上相导线荷载')
wind_load_conductor=project.split*cal_wind_load_conductor(cond, project.Voltage, wind_max, tower.h_top, tower.Lh)
print('线条风荷载:   ',wind_load_conductor)
wind_load_insulator=cal_wind_load_insulator(wind_max, tower.h_top, 0.32)
print('绝缘子风荷载: ',wind_load_insulator)
