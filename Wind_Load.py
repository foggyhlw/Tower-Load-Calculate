#import here
import math
from Universal_Functions import *
from Project_Parameters import *
from Data_Struct import *



#工况气象条件组合
Weather_Condition={ '大风':{'Temperature':10,'V':25,'ice':0},
					'覆冰':{'Temperature':-5,'V':10,'ice':10},
					'低温':{'Temperature':-20,'V':0,'ice':0},
					'高温':{'Temperature':40,'V':0,'ice':0},
					'年平':{'Temperature':15,'V':0,'ice':0},
					'断线':{'Temperature':-5,'V':0,'ice':10},
					'安装':{'Temperature':-10,'V':10,'ice':0}}

#for k,i in Weather_Condition['大风'].items():
#	print(k,i)

#计算导地线风荷载标准值,默认B类地形
#公式见杆塔结构规范2012版P18
#输入Voltage-系统电压 V-风速 H-挂点对地高度 d-线径 mm ground_type-地面粗糙度类别 Lp-水平档距 theta-风向与导地线夹角，ice-冰厚
def cal_wind_load_conductor(Conductor, Weather, H, Lp, theta=90):
	
	alpha=cal_alpha(Weather.V)
	Uz=cal_Uz(H,Weather.ground_type)
	Usc=cal_Usc(Conductor.diameter, Weather.ice)
	Betac=cal_Betac(Weather.V, Conductor.Voltage)
	B1=cal_B(Weather.ice)
	# print(alpha,Uz,Usc,Betac,B1)
	return alpha*Weather.V**2/1600.0*Uz*Usc*Betac*Lp*Conductor.diameter*B1*math.sin(theta)	

#计算绝缘子串风荷载
#V-风速，H-绝缘子串挂点高度，ice-覆冰厚度，A1-绝缘子串受风面积计算值
def cal_wind_load_insulator(Weather, H, As):
	assert(isNmuber(Weather.V))
	assert(isNmuber(H))
	assert(isNmuber(Weather.ice))
	assert(isNmuber(As))

	Uz=cal_Uz(H, Weather.ground_type)
	B1=cal_B(Weather.ice)
	return Weather.V**2/1600.0*Uz*B1*As*1000

####################for test###########################
# wind_load_conductor=cal_wind_load_conductor(cond, wind_max, H, 100)
# print(wind_load_conductor)
# wind_load_insulator=cal_wind_load_insulator(wind_max, H, 0.32)
# print(wind_load_insulator)


