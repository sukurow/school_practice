import sys

argvs = sys.argv
argc = len(argvs)

if(argc != 2):
	print("input error")
	quit()

fr = open(argvs[1] , 'r')

div = fr.read().split()

words = {}

for word in div:
	words[word] = words.get(word, 0) + 1

re = [(v,k) for k,v in words.items()]
re.sort()
re.reverse()
for count, word in re[:10]:
	print count, word


