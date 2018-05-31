# this script takes the output of a blast run
# and outputs a fasta file with the best hit
# to the query in all database files where there is a hit
# as such, it makes sense only to use with single query sequences
# and mainly for databases that are genome files
# to find homologs to one or a set of genes in those genomes

import sys
import re
from Bio.Blast import NCBIXML

blastOutputXMLFile = sys.argv [1]
ProteomeRef=sys.argv[2]
ProteomeTarget=sys.argv[3]

blastOutputXMLHandle = open (blastOutputXMLFile)

listOfBlastRecords = NCBIXML.parse (blastOutputXMLHandle)

for aSingleBlastRecord in listOfBlastRecords:

	for i in range (len (aSingleBlastRecord.alignments)):

		description = aSingleBlastRecord.descriptions [i]
		alignment = aSingleBlastRecord.alignments [i]
		title = re.compile ("gnl\|BL_ORD_ID\|\d* ").sub ("", description.title)
		query = aSingleBlastRecord.query
		
		ID=re.compile ("gnl\|BL_ORD_ID\|").sub ("", description.title)
		IDtrue=[]
		for char in ID:
		    if char.isdigit()==True:
		        IDtrue.append(char)
		    else:
		        break
	
		#print(">" + title)
		#print (ProteomeRef + ":"+alignment.hsps [0].query+" "+ProteomeTarget + ":"+alignment.hsps [0].sbjct)
		#print ('Hit accesion number:', ''.join(IDtrue))
		#print("Reference sequence:   Hit sequence:")
		print (query[2::] + " "+alignment.hsps [0].query+" "+title[2::] + " "+alignment.hsps [0].sbjct)
		break
