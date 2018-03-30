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

cond=Conductor('240/30',3)
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
def critical_span(start, end, step=10):
	#合并字典函数
	def merge_dicts(*dict_args):
	    result = {}
	    for dictionary in dict_args:
	        result.update(dictionary)
	    return result

	for l in range(start, end, step):
		low_temp_fmx=cal_Fmx(cond, low_temp, l)
		hight_temp_fmx=cal_Fmx(cond,high_temp, l)
		ave_temp_fmx=cal_Fmx(cond,ave_temp, l)
		ice_cover_fmx=cal_Fmx(cond,ice_cover, l)
		wind_max_fmx=cal_Fmx(cond,wind_max, l)

		#将所有工况fmx值合并，用于排序求出对应档距下fmx最大的工况
		all_fmx=merge_dicts(low_temp_fmx, hight_temp_fmx, ave_temp_fmx, ice_cover_fmx, wind_max_fmx)
		print(l,'  :  ',max(all_fmx,key=all_fmx.get))	


critical_span(0,500,10)

l=100
def test_fmx():
	print(cal_Fmx(cond, low_temp, l))
	print(cal_Fmx(cond,high_temp, l))
	print(cal_Fmx(cond,ave_temp, l))
	print(cal_Fmx(cond,ice_cover, l))
	print(cal_Fmx(cond,wind_max, l))

test_fmx()
