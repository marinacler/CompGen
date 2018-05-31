import sys, re

# acquire first needed data

geneOrderList = []

aHandle = open (sys.argv [1])

lines = aHandle.readlines ()

for aLine in lines:
	aLine = aLine.replace ("\n", "")

	if aLine.startswith (">"):

		# print aLine [1:len (aLine)],
		geneOrderList.append (aLine [3:len (aLine)])
		#print(aLine [3:len (aLine)])

# acquire second needed data

partOfCluster = {}

bHandle = open (sys.argv [2])

lines = bHandle.readlines ()

id = 0

for aLine in lines:

	aLine = aLine.replace ("\n", "")
	words = aLine.split (" ")
	#words= words.split(" ")
	#print(words)

	for aWord in words:

		#print (aWord)
		if (aWord) not in partOfCluster:

			partOfCluster [aWord] = id

	id = id + 1

# put together
orderedfile=open(sys.argv [1]+'_ordered_list', 'w')
orderedfile2=open(sys.argv [1]+'_ordered', 'w')
for aGene in geneOrderList:

	if aGene in partOfCluster:
		orderedfile.write(str(partOfCluster [aGene])+ ' ')
		orderedfile2.write(str(partOfCluster [aGene])+ '\n')
		#orderedfile.write('\n')
		#print (aGene + ' gene appears in position '+ str(partOfCluster [aGene]) + ' in the ' + sys.argv [2] + ' file')

orderedfile.close()
orderedfile2.close()
