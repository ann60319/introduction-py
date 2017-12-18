name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time=list()
hr=list()
counts=dict()
for line in handle:
	lst=line.split()
	if len(lst)>=1 and lst[0]=="From":
		time.append(lst[5])
		#print(lst[5])
		a=time.split(":")
		hr.append(a[0])
		counts[hr[0]]=counts.get(hr[0],0)+1
	else:
		continue
print (sorted([ (v,k) for k,v in counts.items()]))
