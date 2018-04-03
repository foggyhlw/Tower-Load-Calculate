from math import sqrt,pi
#universal functions here
#判断输入是否为数字
def isNmuber(Number):
	if (type(Number)==int or type(Number)==float):
		return True
	else:
		return False

#风荷载计算
#######################################################################
#通用函数

#计算风压不均匀系数α
#见杆塔结构规范P19
def cal_alpha(V):
	assert(type(V)==int or type(V)==float)
	if (V < 20) :
		return 1.00
	elif ( V < 27) : 
		return 0.85
	elif ( V < 31.5):
		return 0.75
	else:
		return 0.7

#计算导地线风荷载调整系数βc
def cal_Betac(V,Voltage):
	if (Voltage < 500):
		return 1.0
	elif (Voltage>=500 and Voltage<=750):
		if (V <20):
			return 1.00
		elif (V < 27):
			return 1.10
		elif (V < 31.5):
			return 1.20
		else:
			return 1.30

#计算风压高度变化系数μz,默认是B类
def cal_Uz(H,ground_type='B'):
	assert(type(H)==int or type(H)==float)
	assert(type(ground_type)==str)
	if(ground_type=='A'):
		return 1.379*(H/10)**0.24
	elif(ground_type=='B'):
		return 1.000*(H/10)**0.32
	elif(ground_type=='C'):
		return 0.616*(H/10)**0.44
	elif(ground_type=='D'):
		return 0.318*(H/10)**0.60

#计算导地线及绝缘子串覆冰风荷载增大系数B1
#对于大于20mm覆冰，取2.0
def cal_B(ice):
	assert(isNmuber(ice))
	if (ice == 0):
		return 1.0
	elif (ice == 5):
		return 1.1
	elif (ice == 10):
		return 1.2
	elif (ice == 15):
		return 1.3
	elif (ice == 20):
		return 1.5
	else:
		return 2.0

#计算导地线体形系数 d-导线直径，ice-冰厚
def cal_Usc(d,ice):
	assert(type(d)==int or type(d)==float)
	assert(type(ice)==int or type(ice)==float)
	if (ice > 0):
		return 1.2
	if (ice == 0):
		if (d < 17):
			return 1.2
		if (d >= 17):
			return 1.1

######################################################################
#比载计算
 	#计算公式来自新规范中，与大手册在g4,g5计算上有所不同（风荷载计算公式变化导致）
 	#计算不同工况下导地线的比载，因为可能对应多种工况，每次使用重新计算一下即可;
 	#由于比载应用时会根据不同工况进行选择，某一工况下无法得到所有需要的比载值，因此
 	#每次使用时，针对特定工况的特定比载都重新计算一下即可
def cal_g1(Conductor):
 	#自重力荷载g1(N/m),比载gama1(N/m*mm2)
 	g1=9.80665*Conductor.weight_pr_km/1000
 	gama1=g1/Conductor.area
 	return g1,gama1

def cal_g2(Conductor,Weather):
 	#冰重力荷载g2,比载gama2
 	g2=9.80665*0.9*pi*Weather.ice*(Weather.ice+Conductor.diameter)/1000
 	gama2=g2/Conductor.area
 	return g2,gama2

def cal_g3(Conductor, Weather):
 	#自重加冰重力荷载g3,比载gama3
 	g1,gama1=cal_g1(Conductor)
 	g2,gama2=cal_g2(Conductor,Weather)
 	g3=g1+g2
 	gama3=g3/Conductor.area
 	return g3,gama3

#与风压有关的比载，默认规算值线路平均高度Hav
def cal_g4(Conductor,Weather,Hav=15):
 	#无冰时风荷载g4,比载gama4,Hav-线路平均高度 110kV-330kV取15m，500kV取20m
 	#大手册公式：g4=0.625*Weather.V**2*Conductor.diameter*alpha*Usc_no_ice/1000
 	#alpha-风压不均匀系数
 	alpha=cal_alpha(Weather.V)
 	#Usc_no_ice-电线无冰时体型系数
 	Usc_no_ice=cal_Usc(Conductor.diameter,0)
 	#Uz-风压高度变化系数,默认B类
 	Uz=cal_Uz(Hav)
 	g4=Weather.V**2/1600*alpha*Usc_no_ice*Uz*Conductor.diameter
 	gama4=g4/Conductor.area
 	return g4,gama4

def cal_g5(Conductor,Weather,Hav=15):
 	#覆冰时风荷载g5,比载gama5
 	#大手册公式：g5=0.625*Weather.V**2*(Conductor.diameter+2*Weather.ice)*alpha*Usc_ice/1000
 	#alpha-风压不均匀系数
 	alpha=cal_alpha(Weather.V)
 	#Usc_ice-电线覆冰时体型系数
 	Usc_ice=cal_Usc(Conductor.diameter,Weather.ice)
 	#Uz-风压高度变化系数,默认B类
 	Uz=cal_Uz(Hav)
 	#B-导地线覆冰增大系数
 	B=cal_B(Weather.ice)
 	g5=alpha*Weather.V**2/1600*B*(Conductor.diameter+2*Weather.ice)*Usc_ice*Uz
 	gama5=g5/Conductor.area
 	return g5,gama5

def cal_g6(Conductor,Weather,Hav=15):
 	#无冰时综合荷载g6,gama6
 	g1, gama1 = cal_g1(Conductor)	
 	g4, gama4 = cal_g4(Conductor,Weather,Hav)	
 	g6=sqrt(g1**2+g4**2)
 	gama6=g6/Conductor.area
 	return g6,gama6

def cal_g7(Conductor,Weather,Hav=15):
 	#覆冰时综合荷载g7,gama7
 	g3, gama3=cal_g3(Conductor, Weather)	
 	g5, gama5=cal_g5(Conductor,Weather,Hav)	
 	g7=sqrt(g3**2+g5**2)
 	gama7=g7/Conductor.area
 	return g7,gama7
