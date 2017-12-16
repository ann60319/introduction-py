fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
    	line=str
		ipos=line.find(':')
		print(ipos)
