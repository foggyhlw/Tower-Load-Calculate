from Universal_Functions import *
#H为导地线高度
class Project_Info:
	"""docstring for Project"""
	def __init__(self, voltage, tower_type, loop, split):
		#电压等级，以数字形式表示
		self.Voltage = voltage
		#tower_type杆塔形式，1代表直线，2代表耐张
		self.tower_type = tower_type
		#loop 回路数
		self.loop = loop
		#Hav-线路平均高度，110-330取15m，500kV取20m
		if (self.Voltage <= 330):
			self.Hav=15
		if (self.Voltage == 500):
			self.Hav=20	
		#split-导线分裂根数
		self.split=split

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

class Conductor:
	def __init__(self,values,safety_factor,average_factor=0.25):
		'''
		values对应sqlite查询结果中的某一条记录，即用于初始化Conductor类的values变量为查询结果(fetch_all()[n])
		'''
		self.name = values[0]
		#截面积
		self.area = float(values[3])
		#直径
		self.diameter = float(values[4])
		#弹性模量
		self.E = float(values[7])
		#线膨胀系数A（alpha）  (1/°C)*exp-6  
		self.A = float(values[6])*1000000
		#拉断力
		self.Tp = float(values[8])
		#20摄氏度直流电阻
		#self.R = float(values[5])
		#单位质量
		self.weight_pr_km = float(values[9])

		#许用张力Tmax(N),0.95为新线系数
		self.Tmax=self.Tp/safety_factor*0.95
		#许用应力sigma(N/mm2)
		self.sigma_max=self.Tmax/self.area
		#平均运行张力，默认取最大使用张力的25%
		self.Tav=self.Tp*average_factor*0.95
		#平均运行应力
		self.sigma_av=self.Tav/self.area
'''
#导地线类
class Conductor_240:
	def __init__(self, name, voltage, safety_factor, average_factor=0.25):
		#导地线类的生成后续需要从数据库中读出
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

#导地线类  for test
class Conductor_300:
	def __init__(self, name, voltage, safety_factor, average_factor=0.25):
		#导地线类的生成后续需要从数据库中读出
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
'''

#绝缘子串类
class Insulator(object):
	"""从绝缘子库中读取相关参数
		lenth-串长,A1-挡风面积, n-联数"""
	def __init__(self, lenth, As, weight, n):
		self.lenth = lenth
		self.weight = weight
		self.As = As
		self.n = n
		
#气象，地形条件类
class Weather:
	 	"""docstring for We"""
	 	def __init__(self, name, Temperature, Wind_Speed, Ice, Ground_Type='B'):
	 		self.name = name
		 	self.T=Temperature
		 	self.V=Wind_Speed
		 	self.ice=Ice
		 	self.ground_type=Ground_Type



