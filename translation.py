#! /usr/bin/python3
di_ct = { "one":"ATGC", "two" :"TAGC", "three": "GCAT" , "four" : "ATGC", "five" : "GCCAT", "six" : "lys-arg" , "seven" : "GGGcAG" , "eight" : "lys-arg", "nine" : "lys-arg" , "ten" : "lys-arg"}
print(di_ct)
print("\n")

not_in_cluster = []
cluster= []
for key, value in di_ct.items():
	#print('keys are there %s ' % key)
	#print('keys are there  ' , key)
	if value not in not_in_cluster:
		print("%s Not in not_in_cluster "% value)
		not_in_cluster.append(value)
	else :
		print("\n%s ALREADY  in not_in_cluster \n"% value)
		cluster.append(key)
		
print("not_in_cluster there : ", not_in_cluster)
print("cluster there ", cluster)
print("cluster[0] : ", cluster[0])
print("extract relevant key value from dic_t : ")
print (di_ct[cluster[0]]) 
print("\nhow many guys in cluster ", len(cluster))

