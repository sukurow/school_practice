import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 2):
	print('input error')
	quit()

fr = open(argvs[1] , 'r')
row = fr.read()
div = row.split()

for word in div:
	print(word)

fr.close()
