import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
import string

metereologic_variables = ['data','hora','temp_inst','temp_max','temp_min','umid_inst','umid_max','umid_min','pto_orvalho_inst','pto_orvalho_max','pto_orvalho_min','pressao','pressao_max','pressao_min','vento_direcao','vento_vel','vento_rajada','radiacao','precipitacao']
metreologic_drop = ['temp_inst','temp_max','temp_min','umid_inst','umid_max','umid_min','pto_orvalho_inst','pto_orvalho_max','pto_orvalho_min','pressao','pressao_max','pressao_min','vento_direcao','vento_vel','vento_rajada','radiacao', 'hora']

def readMetereologicData():
	df_metereologic = pd.DataFrame.from_csv("../csv/metereologic-data.csv")
	return df_metereologic

def abstractRain(df_meterelogic):
	df_rain = df_meterelogic.copy()
	for var in metreologic_drop:
		df_rain = df_rain.drop(var, 1)
	return df_rain

def rainByDay(df_rain):
	buffer_dict = {}
	for index, row in df_rain.iterrows():
		buffer_dict[row["data"]] = 0

	for index, row in df_rain.iterrows():
		buffer_dict[row["data"]] = buffer_dict[row["data"]] + row["precipitacao"]

	my_dict={}
	for d in buffer_dict:
		vet_split =  d.split("/")
		key = vet_split[2] + "/" + vet_split[1] + "/" + vet_split[0]
		my_dict[key] = buffer_dict[d]

	keylist = my_dict.keys()
	keylist.sort()

	value_list=[]

	for key in keylist:
		print key + " " + str(my_dict[key]) 
		value_list.append(my_dict[key])

	key_list = range(79)

	plt.bar(key_list, value_list, width=0.5, color='g')

	plt.show()

df_meterelogic = readMetereologicData()
df_rain = abstractRain(df_meterelogic)
rainByDay(df_rain)
