import collections
import itertools

filehandle=open('parsedhits_04_16', 'r')
text1=filehandle.read().splitlines()

filehandle2=open('parsedhits_04_18', 'r')
text2=filehandle2.read().splitlines()

filehandle3=open('parsedhits_04_49', 'r')
text3=filehandle3.read().splitlines()

newfile=open('clusteredhits','w')
newfile2=open('clusteredhits_names','w')

dict1=collections.OrderedDict()
dict2=collections.OrderedDict()
dict3=collections.OrderedDict()
dict1_names=collections.OrderedDict()
dict2_names=collections.OrderedDict()
dict3_names=collections.OrderedDict()

filehandle.close()
filehandle2.close()
filehandle3.close()

for sentences in text1:
    line=sentences.split(' ')
    dict1[line[0]]=line[0:4]
    dict1_names[line[0]]=line[2]
    
for sentences in text2:
    line=sentences.split(' ')
    dict2[line[0]]=line[0:4]
    dict2_names[line[0]]=line[2]

for sentences in text3:
    line=sentences.split(' ')
    dict3[line[0]]=line[0:4]
    dict3_names[line[0]]=line[2]


finaldict=collections.OrderedDict()
finaldict_names=collections.OrderedDict()
for k in dict1.keys():
    #print (k)
    if k in dict2.keys():
        if k in dict3.keys():
            addedlist=[dict1[k],dict2[k], dict3[k]]
            addedlist_names=[k, dict1_names[k], dict2_names[k], dict3_names[k]]
            #print (addedlist)
            #print(addedlist_names)
            finaldict[k]=addedlist
            finaldict_names[k]=addedlist_names
            #print(finaldict_names[k])
            #break
        elif k not in dict3.keys():
            addedlist=[dict1[k],dict2[k]]
            addedlist_names=[k, dict1_names[k], dict2_names[k]]
            finaldict[k]=addedlist
            finaldict_names[k]=addedlist_names
                    
    elif k not in dict2.keys():
            if k in dict3.keys():
                addedlist=[dict1[k], dict3[k]]
                addedlist_names=[k, dict1_names[k], dict3_names[k]]
                #print (addedlist)
                #print(addedlist_names)
                finaldict[k]=addedlist
                finaldict_names[k]=addedlist_names
                #print(finaldict_names[k])
                #break
            elif k not in dict3.keys():
                    addedlist=[dict1[k]]
                    addedlist_names=[k, dict1_names[k]]
                    finaldict[k]=addedlist
                    finaldict_names[k]=addedlist_names


for keys in finaldict.keys():
    a=finaldict[keys]
    b=list(itertools.chain.from_iterable(a))
    newfile.write(' '.join(b))
    newfile.write('\n')

for keys in finaldict_names.keys():
    a=finaldict_names[keys]
    newfile2.write(' '.join(a))
    newfile2.write('\n')


newfile.close()
newfile2.close()
#print (dict2['04.fa.txt_orf00002'])
#print (dict3['04.fa.txt_orf00002'])
