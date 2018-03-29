from Data_Struct import *

#计算临界档距的判别式，见大手册P187式3-3-21
def cal_Fmx(Conductor, Weather, l):  
	#不同覆冰情况下比载计算
	if (Weather.ice==0):
		g,gama=cal_g6(Conductor, Weather)
		#print(gama)
	elif (Weather.ice>0):
		g,gama=cal_g7(Conductor, Weather)
		#print(gama)
	else:
		print('Cal_Fmx Weather ice Error!')
	#如果是年平工况，许用应力按百分比法取值，一般为25%
	if (Weather.name=='年平'):
		sigma_max=Conductor.sigma_av
	else:
		sigma_max=Conductor.sigma_max
	#print(Conductor.sigma_max)
	#Conductor.A单位为e-6，公式中除了1000000
	Fmx=Conductor.E*gama**2*l**2/24/sigma_max**2-\
	(sigma_max+Conductor.A/1000000*Conductor.E*Weather.T)
	return dict([(Weather.name,Fmx)])

cond=Conductor('240/30',8)
low_temp=Weather('低温',-20,0,0)
high_temp=Weather('高温',40,0,0)
ice_cover=Weather('覆冰',-5,10,5)
ave_temp=Weather('年平',10,0,0)
wind_max=Weather('大风',10,25,0)
# print(cal_g1(cond))
# print(cal_g2(cond,high_temp))
# print(cal_g3(cond,high_temp))
# print(cal_g4(cond,high_temp))
# print(cal_g5(cond,high_temp))
# print(cal_g6(cond,high_temp))
# print(cal_g7(cond,high_temp))

for l in range(10, 600, 20):
	# print(cal_Fmx(cond, low_temp, l))
	# print(cal_Fmx(cond,high_temp, l))
	# print(cal_Fmx(cond,ave_temp, l))
	# print(cal_Fmx(cond,ice_cover, l))
	# print(cal_Fmx(cond,wind_max, l))
	print(l, cal_Fmx(cond, low_temp, l),
	cal_Fmx(cond,high_temp, l),
	cal_Fmx(cond,ave_temp, l),
	cal_Fmx(cond,ice_cover, l),
	cal_Fmx(cond,wind_max, l))