from Universal_Functions import *
#H为导地线高度


class Conductor:
	def __init__(self,name,safety_factor, average_factor=0.25):
		self.name=name

	#从文件中读取导地线参数，变量前无需加self,因为也无需在该类中新建函数调用其成员变量


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
		self.Tp=75620
		#20摄氏度直流电阻R
		self.R=0.11810
		#许用张力Tmax
		self.Tmax=self.Tp/safety_factor
		#许用应力sigma
		self.sigma_max=self.Tmax/self.area
		#平均运行张力，默认取最大使用张力的25%
		self.Tav=self.Tp*average_factor
		#平均运行应力
		self.sigma_av=self.Tav/self.area


class Weather:
	 	"""docstring for We"""
	 	def __init__(self, name, Temperature, Wind_Speed, Ice,):
	 		self.name = name

		 	self.T=Temperature
		 	self.V=Wind_Speed
		 	self.ice=Ice
	 			
