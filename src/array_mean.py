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

def list_str(vet):
	write = "["
	for i in vet:
		write = write + str(i) + ", "
	return write + "]"



vet = [0,0,5,0,1,3,0,0,0,1,0,0,3]
print vet
print list_str(vet)