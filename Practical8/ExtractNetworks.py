import gzip
#filehandle=gzip.open('protein.links.v10.5.txt.gz', 'r')
#text=filehandle.read().splitlines()
#filehandle.close()
file04=open('04ExtractedNetwork', 'w')
file16=open('16ExtractedNetwork', 'w')
file18=open('18ExtractedNetwork', 'w')
file34=open('34ExtractedNetwork', 'w')
file49=open('49ExtractedNetwork', 'w')


with gzip.open('protein.links.v10.5.txt.gz', 'r') as in_file:
    for line in in_file:
        if line.startswith(b'1037409'):
            file04.write(line.decode('utf-8'))
        elif line.startswith(b'243090'):
            file16.write(line.decode('utf-8'))        
        elif line.startswith(b'1148'):
            file18.write(line.decode('utf-8'))
        elif line.startswith(b'4932'):
            file34.write(line.decode('utf-8'))
        elif line.startswith(b'266117'):
            file49.write(line.decode('utf-8'))
       
file04.close()
file16.close()
file18.close()
file34.close()
file49.close()
