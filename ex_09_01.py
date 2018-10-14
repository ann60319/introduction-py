name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
words=list()
for line in handle:
	lst=line.split()
	if len(lst)>=1 and lst[0]=="From":
		words.append(lst[1])
		#print(lst[1])
	else:
		continue

counts=dict()
for word in words:
	counts[word]=counts.get(word,0)+1

maxvalue=0
maxkey=0
for key,value in counts.items():
	if value>maxvalue:
		maxvalue=value
		maxkey=key
print(maxkey,maxvalue)
