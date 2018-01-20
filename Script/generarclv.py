from itertools import combinations, permutations

def pert(text):
	return list(permutations([text,3],2))




def creartxt():
	outoutfile = open('txt', 'r')
	outfile = open('newc.txt', 'a')
	for n in outoutfile:

		for i in pert(n.strip()):
			print i
			outfile.write(str(i)+'\n')
	outfile.close()
	outoutfile.close()
	print "fin paso"






print "inicia"

creartxt()
