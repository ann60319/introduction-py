fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
ans=0
for line in fh:
	if line.startswith("X-DSPAM-Confidence:") :
		count=count+1
		num=float(line[21:])
		total=num+total
ans=total/count
print("Average spam confidence:",ans)
＃Desired Output
＃Average spam confidence: 0.750718518519
＃Average spam confidence: 0.7507185185185187 mine ave
# http://www.py4e.com/code3/mbox-short.txt
