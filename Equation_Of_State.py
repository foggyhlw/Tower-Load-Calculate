from sympy import Symbol, solveset, S
from Data_Struct import *
from math import cos, pi
#已知某约束条件下的应力，求解另一工况下的导线应力
#################
# 一，悬挂点等高情况下状态方程
#参考大手册P182式3-3-1
# def sol_equation_of_state(l, conductor, weather_known, weather_unknown):
# 	if (weather_known.name=='年平'):
# 		sigma_known=conductor.sigma_av
# 	else:
# 		sigma_known=conductor.sigma_max
# 	#比载使用综合比载
# 	g_known,gama_known=cal_g7(conductor, weather_known)
# 	g_unknown,gama_unknown=cal_g7(conductor, weather_unknown)


# 	a=l**2*gama_known**2*conductor.E/24/sigma_known**2-sigma_known+\
# 		conductor.A/1000000*conductor.E*(weather_unknown.T-weather_known.T)
# 	b=gama_unknown**2*l**2*conductor.E/24

# 	x=Symbol('x')
# 	sigma_unknown=solveset(x**3+a*x**2-b, domain=S.Reals)
# 	print(sigma_unknown)


# 二，悬挂点不等高情况下状态方程
#参考大手册P182式3-3-7
#其思想是利用档距中央应力代替最低点应力，对应悬挂点不等高情况，β为高差角
#该函数已经包括式3-3-1，由于默认情况下beta=0，cos(beta)=1,如果不输入高差角，则就是等高情况下的解
#需要注意，该公式中的档距l和高差角beta对于连续档，都是指的代表档距和代表高差角，详见大手册P182 式3-3-4,3-3-5
def sol_equation_of_state(l, conductor, weather_known, weather_unknown, beta=0):
	if (weather_known.name=='年平'):
		#将许用应力转变为档距中央应力
		sigma_known=conductor.sigma_av/cos(beta/180*pi)
	else:
		sigma_known=conductor.sigma_max/cos(beta/180*pi)
	#比载使用综合比载
	g_known,gama_known=cal_g7(conductor, weather_known)
	g_unknown,gama_unknown=cal_g7(conductor, weather_unknown)
	#中间变量
	a=l**2*gama_known**2*conductor.E/24/sigma_known**2-sigma_known+\
		conductor.A/1000000*conductor.E*(weather_unknown.T-weather_known.T)
	b=gama_unknown**2*l**2*conductor.E/24
	#解方程
	x=Symbol('x')
	sigma_unknown=list(solveset(x**3+a*x**2-b, domain=S.Reals))[0]*cos(beta/180*pi)
	# print(sigma_unknown)
	return sigma_unknown

###################################for test########################
# print(cond.sigma_max)
# sol_equation_of_state(330, cond, ave_temp,ice_cover)
# sol_equation_of_state(330, cond, ave_temp,ice_cover, 5)