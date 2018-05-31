import sys
filename=sys.argv [1] #input example: 04.fa.txt
filehandle=open(filename, 'r')
text=filehandle.read().splitlines()
filehandle.close()
sequence=list(text[1])

################################################################################
### Creating file with the 6 possible reading frames as a FASTA file
################################################################################
readingframes=open('ORFs_'+filename[0:2], 'w')
readingframes.write(text[0]+'_ORF01'+'\n'+''.join(sequence))
readingframes.write('\n'+text[0]+'_ORF02'+'\n'+''.join(sequence[1:]))
readingframes.write('\n'+text[0]+'_ORF03'+'\n'+''.join(sequence[2:]))
complementary=[]
for i in range (0, len(sequence)):
    if sequence [i] == 'A':
        complementary.append('T')
    elif sequence [i] == 'T':
        complementary.append('A')
    elif sequence [i] == 'C':
        complementary.append('G')
    elif sequence [i] == 'G':
        complementary.append('C')
    if sequence [i] == 'N':
        complementary.append('N')
readingframes.write('\n'+text[0]+'_ORF04'+'\n'+''.join(complementary))
readingframes.write('\n'+text[0]+'_ORF05'+'\n'+''.join(complementary[1:]))
readingframes.write('\n'+text[0]+'_ORF06'+'\n'+''.join(complementary[2:]))
readingframes.close()

################################################################################
### Creating file with predicted ORFs as a FASTA file
################################################################################
filehandle2=open('ORFs_'+filename[0:2], 'r')
text2=filehandle2.read().splitlines()
filehandle2.close()
PossibleORFs=open(filename[0:2]+'_ORFs_AlternativeSTART', 'w') #eukaryote: PossibleORFs=open(filename[0:2]+'_ORFs', 'w')

numberORF=0
totalpossibleORFs=0
for line in range(1,12,2):
    seq=text2[line]
    lastposition=0 #to know where to start looking from for an ATG
    for j in range(0, len(seq),3):
        ORFseq=[]
        if j >= lastposition: #that way we keep the longer ORFs and discard the overlapping ones that are shorter
            if seq[j:j+3] == 'ATG' or seq[j:j+3] == 'GTG' or seq[j:j+3] == 'TTG' or seq[j:j+3] == 'ATA' :  #eukaryote: if seq[j:j+3] == 'ATG':
                for k in range(j, len(seq),3):
                    if seq[k:k+3] != 'TAA' and seq[k:k+3] !='TAG' and seq[k:k+3] !='TGA':
                        ORFseq.append(seq[k:k+3])
                        if seq[k:k+3] == 'ATG' or seq[k:k+3] == 'GTG' or seq[k:k+3] == 'TTG' or seq[k:k+3] == 'ATA' :  #eukaryote: if seq[k:k+3] == 'ATG':
                            if 'TAA'in seq[k+3:]:
                                totalpossibleORFs=totalpossibleORFs+1       
                            elif 'TAG' in seq[k+3:]:
                                totalpossibleORFs=totalpossibleORFs+1
                            elif 'TGA' in seq[k+3:]:
                                    totalpossibleORFs=totalpossibleORFs+1
                    elif seq[k:k+3] == 'TAA' or seq[k:k+3] =='TAG' or seq[k:k+3] =='TGA':
                        #ORFseq.append(seq[k:k+3])
                        break
                        
                if len(ORFseq)>=200:
                    numberORF=numberORF+1
                    lastposition=k+3
                    PossibleORFs.write(text2[line-1]+'_'+str(numberORF)+'\n')
                    PossibleORFs.write(''.join(list(ORFseq))+'\n')

PossibleORFs.close()
TN=totalpossibleORFs-numberORF
print('True negative: '+ str(TN))

################################################################################
### Including TATA box, which gave worse results
################################################################################
                             
                #if len(ORFseq)>=200:
                #    if (k+3-len(ORFseq))>=60:
                #        if 'TATA' in seq[(k+3-len(ORFseq)-60):(k+3-len(ORFseq))]:
                #            numberORF=numberORF+1
                #            lastposition=k+3
                #            PossibleORFs.write(text2[line-1]+'_'+str(numberORF)+'\n')
                #            PossibleORFs.write(''.join(list(ORFseq))+'\n')

                #    elif (k+3-len(ORFseq))<60:
                #        numberORF=numberORF+1
                #        lastposition=k+3
                #        PossibleORFs.write(text2[line-1]+'_'+str(numberORF)+'\n')
                #        PossibleORFs.write(''.join(list(ORFseq))+'\n')
           

################################################################################
### Translating
################################################################################
ORFsTranslated=open(filename[0:2]+'_ORFs_AlternativeSTART_AA', 'w') #eukaryote: ORFsTranslated=open(filename[0:2]+'_ORFs_AA', 'w')
filetotranslate=open(filename[0:2]+'_ORFs_AlternativeSTART', 'r') #eukaryote: filetotranslate=open(filename[0:2]+'_ORFs', 'r')
text3=filetotranslate.read().splitlines()
filetotranslate.close()

aminoacids={}
aminoacids['A']=['GCT','GCC','GCA','GCG']
aminoacids['R']=['CGT','CGC','CGA','CGG','AGA','AGG']
aminoacids['N']=['AAT','AAC']
aminoacids['D']=['GAT','GAC']
aminoacids['C']=['TGT','TGC']
aminoacids['Q']=['CAA','CAG']
aminoacids['E']=['GAA','GAG']
aminoacids['G']=['GGT','GGC','GGA','GGG']
aminoacids['H']=['CAT','CAC']
aminoacids['I']=['ATT','ATC','ATA']
aminoacids['L']=['TTA','TTG','CTT','CTC','CTA', 'CTG']
aminoacids['K']=['AAA','AAG']
aminoacids['M']=['ATG']
aminoacids['F']=['TTT','TTC']
aminoacids['P']=['CCT','CCC','CCA','CCG']
aminoacids['S']=['TCT','TCC','TCA','TCG','AGT','AGC']
aminoacids['T']=['ACT','ACC','ACA','ACG']
aminoacids['W']=['TGG']
aminoacids['Y']=['TAT','TAC']
aminoacids['V']=['GTT','GTC','GTA','GTG']
aminoacids['*']=['TAA','TAG','TGA'] #stop codon

for linenum in range(0,len(text3)):
    if text3[linenum].startswith('>'):
        ORFsTranslated.write(text3[linenum]+'\n')
        sequence=text3[linenum+1]
        sequenceTranslated=[]
        for i in range(0, len(sequence),3):
            codon=sequence[i:i+3]
            codon=''.join(codon)
            #print(codon)
            #codon in [x for v in dic.values() for x in v]
            for aminoacid in aminoacids.keys():
                if codon in aminoacids[aminoacid]:
                    sequenceTranslated.append(aminoacid)
        ORFsTranslated.write(''.join(list(sequenceTranslated))+'\n')
ORFsTranslated.close()
