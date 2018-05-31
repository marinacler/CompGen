filehandle=open('randomsequences', 'r')
text=filehandle.read().splitlines()
filehandle.close()

multiFASTA=open('multiFASTA_pseudogenomes', 'w')

filenames=['04','16','18','49']
for i in filenames:
    filehandle2=open(str(i)+'.fa.txt.pfa_ordered', 'r')
    text2=filehandle2.read().splitlines()
    filehandle2.close()
    multiFASTA.write('>'+'pseudogene'+str(i)+'\n')
    filetowrite=open(str(i)+'.fa.txt.pfa_pseudogenome', 'w')
    for position in text2:
        filetowrite.write(text[int(position)])
        multiFASTA.write(text[int(position)])
    filetowrite.close()
    multiFASTA.write('\n')
    
multiFASTA.close()
