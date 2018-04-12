import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 3):
	print('not input error')
	quit()

fo = open(argvs[1],'r')
fw = open(argvs[2],'w')
list = fo.read()
fw.write(list)

fo.close()
fw.close()

