import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 2):
	print('not file name')
	quit()

f = open(argvs[1])

for row in f:
	print row.strip()

f.close()
 
