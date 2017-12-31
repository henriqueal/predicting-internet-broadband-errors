#quantidade de chuva interfere? qtd por hora interefere? cor(att, snr)? Umidade interfere?
#quais as dores? eh o sinal ruido, eh a taxa de atenuacao, oq intefere?
#dores: dificil conversar com pessoas, elas trabalham e n tem tmepo dados incompletos.

import json, mechanize
import operator
import random
from split_ip import read_ips

def process_zeros(vet):
	j=0
	for i in vet:
		if(i==-1 or i==None):
			vet[j] = 0
		j = j + 1
	return vet

def is_vet_null(vet):
	for v in vet:
		if v!=0:
			return False
	return True

def write_file(my_path, my_text):
	arq = open(my_path, 'w')
	arq.write(my_text)
	arq.close()

def write_file_list(my_path, my_text):
	arq = open(my_path, 'w')
	arq.writelines(my_text)
	arq.close()

def read_json(ip):
	br = mechanize.Browser()
	r = br.open("http://172.20.4.169:8080/dslams-extractor/service/dslams/" + ip + "?snapshotsNum=15")
	return json.loads(r.read())

def array_mean(vet):
	for i in range(len(vet)):
		for j in range(len(vet)):
			if vet[j] == 0:
				if j==0:
					vet[j] = vet[j+1]
				elif (j==(len(vet)-1)):
					vet[j] = vet[j-1]
				else:
					vet[j] = (vet[j-1] + vet[j+1])/2.0
					if vet[j-1] == 0:
						vet[j] = vet[j+1]
					elif vet[j+1] == 0:
						vet[j] = vet[j-1]
	return vet

def get_index_by_date(ports_random):
	date = ports_random[k]["portSnapshots"][m]["creationDate"]
	a = ports_random[k]["portSnapshots"][m]["creationDate"].split(" ")
	x=2
	vet = [a[0][i:i+x] for i in range(0, len(a[0]), x)]
	z = int(vet[4])-first_day_measurement
	return z

def list_str(vet):
	write = "["
	for i in vet:
		write = write + str(i) + ", "
	return write + "]"

##variables
repetions = 10
n_ips = 10
n_ports = 10
n_rain = 16
first_day_measurement = 14
split_date = 2
write = ""
write_mod = ""


##definir o vetor que vai acumular todos os vetores das atenuacoes
vet_att_all = []
vet_att_null = []
vet_att_wout_null = []
vet_att_wout_null_mean = []
for r in range(repetions):

	## sort n Ips and write in file
	rows = read_ips()
	ips_random = random.sample(rows,  n_ips)
	my_path = '../out/lista-ips.txt'
	write_file_list(my_path, ips_random)

	#open urls
	for ip in ips_random:
		measurements = read_json(ip)	 
		##caso a quantidade maxima de portas daquele ip for menor que 
		##a quantidade definida por n_ports. entao alterar o tamanho de n_ports
		##para o tamanho maximo de qtd de portas do ip
		if len(measurements["ports"]) < n_ports:
			n_ports = len(measurements["ports"])
		
		##sorteia n_ports aleatoriamente
		ports_random = random.sample(measurements["ports"], n_ports)
			
		for k in range(n_ports):
			vet_att=[]	
			for i in range(n_rain):
				vet_att.append(-1)

			for m in range(len(ports_random[k]["portSnapshots"])):
				##definir valores padroes para o vetor de attenuable
				z = get_index_by_date(ports_random)
				vet_att[z] = ports_random[k]["portSnapshots"][m]["attenuationDown"]
			
			vet_att = process_zeros(vet_att)
			vet_att_all.append(vet_att)
			if (is_vet_null(vet_att)):
				vet_att_null.append(ip + "_" + ports_random[k]["name"])
			else:
				vet_att_wout_null.append(vet_att)
				vet_att = array_mean(vet_att)
				vet_att_wout_null_mean.append(vet_att)
				write_mod = write_mod + (str(r)+";"+ip+";"+ports_random[k]["name"]+";"+list_str(vet_att)) + "\n"

			write = write + (str(r)+";"+ip+";"+ports_random[k]["name"]+";"+list_str(vet_att)) + "\n"
		

#arq=open('../out/vet_att_null.txt', 'w')
#arq.writelines(vet_att_null)
#arq.close()

my_string = "quantidade de ips: " + str(len(ips_random)) +".\n"
my_string = my_string +"quantidade de portas testadas: " + str(len(vet_att_all)) +".\n"
my_string = my_string +"quantidade com null: " + str(len(vet_att_null)) +".\n"
my_string = my_string +"quantidade sem null: " + str(len(vet_att_wout_null)) + ".\n"

arq=open('../out/sumary.txt', 'w')
arq.writelines(my_string)
arq.close()

#print "vet_att_all"
#print vet_att_all
#print "vet_att_wout_null"
#print vet_att_wout_null

write_file('../out/write_mod.txt', write_mod)
write_file('../out/write.txt', write)
