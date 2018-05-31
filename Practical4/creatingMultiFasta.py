filehandle=open('clusteredhits_names', 'r')
text1=filehandle.read().splitlines()
filehandle.close()
for i in range(0,10):  #we want 10 different ortholog clusters for exercise 7, so just selected the first ones
    FASTAfile=open(str(i+1)+'cluster', 'w')
    text1[i] = text1[i].split(" ")
    for element in text1[i]:
        #print(element)
        filepfa=open(element[0:9]+'.pfa', 'r')
        textpfa=filepfa.read().splitlines()
        filepfa.close()
        counter=0
        FASTAfile.write('>'+element)
        FASTAfile.write('\n')
        for line in textpfa:
            if line == '>./'+element:
                counter=counter+1
                while textpfa[counter].startswith('>')==False:
                    FASTAfile.write(textpfa[counter])
                    FASTAfile.write('\n')
                    counter=counter+1   
            else:
                counter=counter+1
        #FASTAfile.write('\n')
