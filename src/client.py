import pandas as pd
from iplist import vet



def readIpList():
	print "teste"
	#df_ip = pd.from_csv("../csv/ip-list-list.csv")
	df = pd.read_csv('../csv/ip-list-list.csv', delimiter=',')
	dicts = df.to_dict().values()
	#print df

def readClientsData():
	print ("client data")

def addColunmMeditionByClient():
	print ("medition by client")

def howManyClients():
	print ("we have K clients")

def addColunmStatistics():
	print ("statistcs")

def correlationRainMedition():
	print ("corr")


readIpList()
print vet

readClientsData()
addColunmStatistics()
howManyClients()
addColunmMeditionByClient()
correlationRainMedition()