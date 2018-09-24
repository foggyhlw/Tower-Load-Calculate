from Data_Struct import *
import sqlite3
conductor_type = 'LGJ-240/30'
#在数据库中查找导线相关参数
conn = sqlite3.connect('./database/wires.db')
cursor = conn.cursor()
cursor.execute("select * from wire where N= '{}'".format(conductor_type))
values = cursor.fetchall()
cursor.close()
conn.close()

################for test##########################	 			
project=Project_Info(220, 2, 1, 2)
tower=Tower(190, 273, 378, 278)
tower.set_hang_points(27, 27, 27)
#cond=Conductor('240/30', 110, 3 )
#cond=Conductor_300('300/40', 220, 2.5)
cond = Conductor(values[0],2.5)
#气象条件设置
low_temp=Weather('低温', -20, 0, 0, 'B')
high_temp=Weather('高温', 40, 0, 0, 'B')
ice_cover=Weather('覆冰', -5, 10, 5, 'B')
ave_temp=Weather('年平', 10, 0, 0, 'B')
wind_max=Weather('大风', -5, 25, 0, 'B')
cond_install=Weather('安装', -20, 10, 0, 'B')
check_condition=Weather('验算', -5, 10, 10, 'B')
#weather_dict用于通过工况名称查询对应工况信息
weather_dict={'低温':low_temp, '高温':high_temp, '年平':ave_temp,\
'覆冰':ice_cover, '大风':wind_max, '安装': cond_install, '验算':check_condition}
