fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
	lst=line.split()
	if len(lst)>=2 and lst[0]=='From':
		count=count+1
		print(lst[1])
	else:
		continue
print("There were", count, "lines in the file with From as the first word")
