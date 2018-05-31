filehandle04=open('04.fa.txt.pfa', 'r')
text04=filehandle04.read().splitlines()

filehandle16=open('16.fa.txt.pfa', 'r')
text16=filehandle16.read().splitlines()

filehandle18=open('18.fa.txt.pfa', 'r')
text18=filehandle18.read().splitlines()

filehandle49=open('49.fa.txt.pfa', 'r')
text49=filehandle49.read().splitlines()

filehandle04.close()
filehandle16.close()
filehandle18.close()
filehandle49.close()

counter04=0
counter16=0
counter18=0
counter49=0
for lines in text04:
    if lines.startswith('>'):
        counter04=counter04+1
for lines in text16:
    if lines.startswith('>'):
        counter16=counter16+1
for lines in text18:
    if lines.startswith('>'):
        counter18=counter18+1
for lines in text49:
    if lines.startswith('>'):
        counter49=counter49+1
        
print('Counter 4 is :' + str(counter04))
print('Counter 16 is :' + str(counter16))
print('Counter 18 is :' + str(counter18))
print('Counter 49 is :' + str(counter49))
