from Universal_Functions import *
#H为导地线高度
class Project_Info:
	"""docstring for Project"""
	def __init__(self, voltage, tower_type, loop, split):
		#电压等级，以数字形式表示
		self.voltage = voltage
		#tower_type杆塔形式，1代表直线，2代表耐张
		self.tower_type = tower_type
		#loop 回路数
		self.loop = loop
		#Hav-线路平均高度，110-330取15m，500kV取20m
		if (self.voltage <= 330):
			self.Hav=15
		if (self.voltage == 500):
			self.Hav=20	
		#split-导线分裂根数
		self.split=split
#相应设置函数，用于configure
	def set_voltage(self, voltage):
		self.voltage = voltage

	def set_tower_type(self, tower_type):
		self.tower_type = tower_type

	def set_loop(self, loop):
		self.loop = loop

	def set_split(self, split):
		self.split = split

	def set_Hav(self, Hav):
		self.Hav = Hav

class Tower:
	"""杆塔档距相关参数，其中水平档距固定，垂直档距随工况不同而有变化"""
	def __init__(self, Lh, Lv, Lr_front, Lr_back):
	#水平档距Lh,垂直档距Lv,代表档距Lr
		self.Lh = Lh
		self.Lv = Lv
		self.Lr_front = Lr_front
		self.Lr_back = Lr_back

	#设置挂点高度	,下-中-上
	def set_hang_points(self, h_bottom, h_medium, h_top):
		self.h_bottom = h_bottom
		self.h_medium = h_medium
		self.h_top= h_top

	#设置函数，用于configure
	#前后侧水平档距
	def set_Lh_front(self, Lh_front):
		self.Lh_front = Lh_front

	def set_Lh_back(self, Lh_back):
		self.Lh_back = Lh_back
	#前后侧垂直档距
	def set_Lv_front(self, Lv_front):
		self.Lv_front = Lv_front

	def set_Lv_back(self, Lv_back):
		self.Lv_back = Lv_back
	#前后侧代表档距
	def set_Lr_front(self, Lr_front):
		self.Lr_front = Lr_front

	def set_Lr_back(self, Lr_back):
		self.Lr_back = Lr_back

#导地线类
class Conductor_240:
	def __init__(self, name, voltage, safety_factor, average_factor=0.25):
		'''导地线类的生成后续需要从数据库中读出'''
		self.name=name
		#直径 mm
		self.diameter=21.6
		#单位重量（kg/km)
		self.weight_pr_km=922.2
		#截面积(mm2)
		self.area=275.96
		#弹性模量E(N/mm2)
		self.E=73000
		#线膨胀系数A（alpha）  (1/°C)*exp-6  
		self.A=19.6          #(使用时注意单位换算exp-6)
		#拉断力 Tp(N)
		self.Tp=75190
		#20摄氏度直流电阻R
		self.R=0.11810
		#许用张力Tmax(N),0.95为新线系数
		self.Tmax=self.Tp/safety_factor*0.95
		#许用应力sigma(N/mm2)
		self.sigma_max=self.Tmax/self.area
		#平均运行张力，默认取最大使用张力的25%
		self.Tav=self.Tp*average_factor*0.95
		#平均运行应力
		self.sigma_av=self.Tav/self.area
		#线路电压等级
		self.Voltage=voltage

	def read_from_db(self, name):
		pass

#导地线类  for test
class Conductor_300:
	def __init__(self, name, voltage, safety_factor, average_factor=0.25):
		'''导地线类的生成后续需要从数据库中读出'''
		self.name=name
		#直径 mm
		self.diameter=23.94
		#单位重量（kg/km)
		self.weight_pr_km=1133
		#截面积(mm2)
		self.area=338.99
		#弹性模量E(N/mm2)
		self.E=73000
		#线膨胀系数A（alpha）  (1/°C)*exp-6  
		self.A=19.6          #(使用时注意单位换算exp-6)
		#拉断力 Tp(N)
		self.Tp=92220
		#20摄氏度直流电阻R
		self.R=0.09614
		#许用张力Tmax(N),0.95为新线系数
		self.Tmax=self.Tp/safety_factor*0.95
		#许用应力sigma(N/mm2)
		self.sigma_max=self.Tmax/self.area
		#平均运行张力，默认取最大使用张力的25%
		self.Tav=self.Tp*average_factor*0.95
		#平均运行应力
		self.sigma_av=self.Tav/self.area
		#线路电压等级
		self.Voltage=voltage

#绝缘子串类
class Insulator(object):
	"""从绝缘子库中读取相关参数
		lenth-串长,A1-挡风面积, n-联数"""
	def __init__(self, lenth, As, weight, n):
		self.lenth = lenth
		self.weight = weight
		self.As = As
		self.n = n

	def read_from_db(self, name):
		pass
		
#气象，地形条件类
class Weather:
	"""docstring for We"""
	def __init__(self, name, Temperature, Wind_Speed, Ice, Ground_Type='B'):
		self.name = name
		self.T =  Temperature
		self.V = Wind_Speed
		self.ice = Ice
		self.ground_type = Ground_Type

	def read_from_db(self, name):
		pass

	def set_weather(self, name, Temperature, Wind_Speed, Ice):
 		self.name = name
	 	self.T = Temperature
	 	self.V = Wind_Speed
	 	self.ice = Ice

	def set_ground_type(self, ground_type):
		self.ground_type = ground_type

################for test##########################	 			
project=Project_Info(220, 2, 1, 2)
tower=Tower(190, 273, 378, 278)
tower.set_hang_points(27, 27, 27)
#cond=Conductor('240/30', 110, 3 )
cond=Conductor_300('300/40', 220, 2.5)
low_temp=Weather('低温', -20, 0, 0, 'B')
high_temp=Weather('高温', 40, 0, 0, 'B')
ice_cover=Weather('覆冰', -5, 10, 5, 'B')
ave_temp=Weather('年平', 10, 0, 0, 'B')
wind_max=Weather('大风', -5, 25, 0, 'B')
cond_install=Weather('安装', -20, 10, 0, 'B')
check_condition=Weather('验算', -5, 10, 15, 'B')
#weather_dict用于通过工况名称查询对应工况信息
weather_dict={'低温':low_temp, '高温':high_temp, '年平':ave_temp,\
'覆冰':ice_cover, '大风':wind_max, '安装': cond_install, '验算':check_condition}