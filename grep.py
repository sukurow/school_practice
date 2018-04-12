import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 3):
	print('input error')
	quit()

fr = open(argvs[1],'r')
line = fr.readline()
while line:
	if(argvs[2] in line):
		print(line)
	line = fr.readline()
