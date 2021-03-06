from Project_Parameters import *

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


#工具函数
#合并字典函数
def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def critical_span(start, end, step=10, allow_ave_control=True):

	critical_span_list={}
	for l in range(start, end, step):
		low_temp_fmx=cal_Fmx(cond, low_temp, l)
		hight_temp_fmx=cal_Fmx(cond,high_temp, l)
		ave_temp_fmx=cal_Fmx(cond,ave_temp, l)
		ice_cover_fmx=cal_Fmx(cond,ice_cover, l)
		wind_max_fmx=cal_Fmx(cond,wind_max, l)

		#将所有工况fmx值合并，用于排序求出对应档距下fmx最大的工况
		if (allow_ave_control == True):
			all_fmx=merge_dicts(low_temp_fmx, hight_temp_fmx, ave_temp_fmx, ice_cover_fmx, wind_max_fmx)
			# print('允许年平控制')
		else:
			all_fmx=merge_dicts(low_temp_fmx, hight_temp_fmx, ice_cover_fmx, wind_max_fmx)
			# print('不允许年平控制')
		print(l,'  :  ',max(all_fmx, key = all_fmx.get))	

#找出某档距l下Fmx最大者，即控制工况,返回对应工况的名称
#此处
def find_control_condition(l, allow_ave_control=True ):

	low_temp_fmx=cal_Fmx(cond, low_temp, l)
	hight_temp_fmx=cal_Fmx(cond,high_temp, l)
	ave_temp_fmx=cal_Fmx(cond,ave_temp, l)
	ice_cover_fmx=cal_Fmx(cond,ice_cover, l)
	wind_max_fmx=cal_Fmx(cond,wind_max, l)
	if( allow_ave_control==True ):
		all_fmx=merge_dicts(low_temp_fmx, hight_temp_fmx, ave_temp_fmx, ice_cover_fmx, wind_max_fmx)
		# print('允许年平控制')
	else:
		all_fmx=merge_dicts(low_temp_fmx, hight_temp_fmx, ice_cover_fmx, wind_max_fmx)
		# print('不适用年平控制')

	return(max(all_fmx,key=all_fmx.get))

#######################for test#########################
print(find_control_condition(170, False))
critical_span(0,300,10, False)

# l=100
# def test_fmx():
# 	print(cal_Fmx(cond, low_temp, l))
# 	print(cal_Fmx(cond,high_temp, l))
# 	print(cal_Fmx(cond,ave_temp, l))
# 	print(cal_Fmx(cond,ice_cover, l))
# 	print(cal_Fmx(cond,wind_max, l))

# test_fmx()

# print(cal_g1(cond))
# print(cal_g2(cond,high_temp))
# print(cal_g3(cond,high_temp))
# print(cal_g4(cond,high_temp))
# print(cal_g5(cond,high_temp))
# print(cal_g6(cond,high_temp))
# print(cal_g7(cond,high_temp))