import csv

def split_ip(ip):
	line = ip
	n = 3
	vet = [line[i:i+n] for i in range(0, len(line), n)]
	s = ""

	i=0
	for v in vet:
		if i != 0:
			s = s + "."
		s = s + str(int(v))
		i = i + 1
	print s

def read_ips():
	with open('../csv/ips_udi_modified.csv') as csvfile:
	    readCSV = csv.reader(csvfile, delimiter=',')
	    rows = []
	    for row in readCSV:
	        rows.append(row[0])
	    return rows

#ows = read_ips()
#for row in rows:
	#ip = split_ip(row)
