import sys
import math
filename=sys.argv [1] #input example: 04_ORFs_AlternativeSTART
filehandle=open(filename, 'r')
text=filehandle.read().splitlines()
filehandle.close()

################################################################################
### Extracting our predicted ORFs and the ones predicted by GLIMMER
################################################################################
genomenumber=filename[0:2]
if genomenumber=='34':
    fileGlimmer=open(genomenumber+'_GENSCAN.txt', 'r')
else:
    fileGlimmer=open(genomenumber+'_GLIMMER.longorf', 'r')
textGlimmer=fileGlimmer.read().splitlines()
fileGlimmer.close()
GlimmerORFs=[]
if genomenumber != '34':
    for i in range(0, len(textGlimmer)):
        if textGlimmer[i].startswith(">"):
            GlimmerORFs.append(textGlimmer[i+1])
elif genomenumber=='34':
    for i in range(0, len(textGlimmer)):
        if textGlimmer[i].startswith(">"):
            if textGlimmer[i+1].startswith('ATG') or textGlimmer[i+1].startswith('atg'):
                GlimmerORFs.append(textGlimmer[i+1])      
MyORFs=[]
for i in range(0, len(text)):
    if text[i].startswith(">"):
        orf=text[i+1]
        MyORFs.append(orf[0:60])

################################################################################
### Calculating TP, TN, FP, FN, specificity and MCC
################################################################################
#values obtained from the ORFfinder.py script
if filename[0:2] == '04':
    TN= 20026
elif filename[0:2] == '16':
    TN= 17419
elif filename[0:2] == '18':
    TN= 10123
elif filename[0:2] == '34':
    TN= 34941
elif filename[0:2] == '49':
    TN= 46585
TP=0
FN=0
FP=0
for sequence in GlimmerORFs:
    if genomenumber=='34':
        if sequence in (name.lower() for name in MyORFs):
            TP=TP+1
        else:
            FN=FN+1
    else:
        if sequence in MyORFs:
            TP=TP+1
        else:
            FN=FN+1
for sequence2 in MyORFs:
    if genomenumber=='34':
        if sequence2 not in (name.upper() for name in GlimmerORFs):
            FP=FP+1
    else:
        if sequence2 not in GlimmerORFs:
            FP=FP+1

print('TP: ' + str(TP) + ' FN: '+ str(FN) + ' FP: '+ str(FP))
Sensitivity="{0:.2f}".format(TP/(TP+FN))
Specificity="{0:.2f}".format(TP/(TP+FP))
Specificity2="{0:.2f}".format(TN/(TN+FP))
print ('The sensitivity is '+str(Sensitivity))
print ('The specificity is '+str(Specificity))
print ('The real specificity is '+str(Specificity2))
MCC=((TP*TN)-(FN*FP))/(math.sqrt((TP+FN)*(TN+FP)*(TP+FP)*(TN+FN)))
print('The MCC is: '+str(round(MCC,2)))
