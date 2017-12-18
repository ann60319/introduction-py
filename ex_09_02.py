name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hr=list()
counts=dict()
for line in handle:
	lst=line.split()
	if len(lst)>=1 and lst[0]=="From":
		x=lst[5].split(":")
		hr.append(x[0])
		#print(x[0])
		counts[x[0]]=counts.get(x[0],0)+1
	else:
		continue
k=list()
for key,value in counts.items():
	l=(key,value)
	k.append(l)
k=sorted(k)
for key,value in k:
	print(key,value)
