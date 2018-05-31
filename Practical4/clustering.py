import collections
import itertools

filehandle=open('parsedhits_04_16', 'r')
text1=filehandle.read().splitlines()

filehandle2=open('parsedhits_04_18', 'r')
text2=filehandle2.read().splitlines()

filehandle3=open('parsedhits_04_49', 'r')
text3=filehandle3.read().splitlines()

newfile=open('clusteredhits','w')

dict1=collections.OrderedDict()
dict2=collections.OrderedDict()
dict3=collections.OrderedDict()

filehandle.close()
filehandle2.close()
filehandle3.close()

for sentences in text1:
    line=sentences.split(' ')
    dict1[line[0]]=line[0:4]

for sentences in text2:
    line=sentences.split(' ')
    dict2[line[0]]=line[0:4]

for sentences in text3:
    line=sentences.split(' ')
    dict3[line[0]]=line[0:4]


finaldict=collections.OrderedDict()
for k in dict1.keys():
    #print (k)
    for j in dict2.keys():
        #print(j)
        if k==j:
            for l in dict3.keys():
                if k ==l:
                    addedlist=[dict1[k],dict2[j], dict3[l]]
                    #print (addedlist)
                    finaldict[k]=addedlist
                    break
                #else:
                    #addedlist=[dict1[k],dict2[j], dict3[l]]
                    #finaldict[k]=addedlist
                    
        else:
            #finaldict[k]=dict1[k]
            

            #print (addedlist)
            finaldict[k]=addedlist

for keys in finaldict.keys():
    a=finaldict[keys]
    b=list(itertools.chain.from_iterable(a))
    newfile.write(' '.join(b))
    newfile.write('\n')

newfile.close()
#print (dict2['04.fa.txt_orf00002'])
#print (dict3['04.fa.txt_orf00002'])
