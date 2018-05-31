import numpy as np
import math

################################################################################
### GC frequencies
################################################################################

GC04=63.05
GC16=55.48
GC18=47.55
GC34=38.64
GC49=70.48

distancematrix=np.zeros((5,5))
distance0416=math.sqrt((GC04-GC16)**2)
distance0418=math.sqrt((GC04-GC18)**2)
distance0434=math.sqrt((GC04-GC34)**2)
distance0449=math.sqrt((GC04-GC49)**2)
distance1618=math.sqrt((GC16-GC18)**2)
distance1634=math.sqrt((GC16-GC34)**2)
distance1649=math.sqrt((GC16-GC49)**2)
distance1834=math.sqrt((GC18-GC34)**2)
distance1849=math.sqrt((GC18-GC49)**2)
distance3449=math.sqrt((GC34-GC49)**2)
distancematrix[0][1]=distancematrix[1][0]=round(distance0416,2)
distancematrix[0][2]=distancematrix[2][0]=round(distance0418,2)
distancematrix[0][3]=distancematrix[3][0]=round(distance0434,2)
distancematrix[0][4]=distancematrix[4][0]=round(distance0449,2)
distancematrix[1][2]=distancematrix[2][1]=round(distance1618,2)
distancematrix[1][3]=distancematrix[3][1]=round(distance1634,2)
distancematrix[2][3]=distancematrix[3][2]=round(distance1649,2)
distancematrix[2][4]=distancematrix[4][2]=round(distance1849,2)
distancematrix[3][4]=distancematrix[4][3]=round(distance3449,2)

GCfile=open("GCdistancematrix","w")
GCfile.write("Genome04 Genome16 Genome18 Genome34 Genome49""\n")
GCfile.write(str(distancematrix))
GCfile.close()

################################################################################
### Nucleotide frequencies
################################################################################

A04=18.48
C04=31.48
G04=31.57
T04=18.47
A16=22.24
C16=27.72
G16=27.77
T16=22.28
A18=26.34
C18=23.76
G18=23.78
T18=26.11
A34=30.8
C34=19.34
G34=19.3
T34=30.56
A49=14.78
C49=35.34
G49=35.14
T49=14.75

distancematrix2=np.zeros((5,5))
nucldistance0416=math.sqrt((A04-A16)**2+(C04-C16)**2+(G04-G16)**2+(T04-T16)**2)
nucldistance0418=math.sqrt((A04-A18)**2+(C04-C18)**2+(G04-G18)**2+(T04-T18)**2)
nucldistance0434=math.sqrt((A04-A34)**2+(C04-C34)**2+(G04-G34)**2+(T04-T34)**2)
nucldistance0449=math.sqrt((A04-A49)**2+(C04-C49)**2+(G04-G49)**2+(T04-T49)**2)
nucldistance1618=math.sqrt((A16-A18)**2+(C16-C18)**2+(G16-G18)**2+(T16-T18)**2)
nucldistance1634=math.sqrt((A16-A34)**2+(C16-C34)**2+(G16-G34)**2+(T16-T34)**2)
nucldistance1649=math.sqrt((A16-A49)**2+(C16-C49)**2+(G16-G49)**2+(T16-T49)**2)
nucldistance1834=math.sqrt((A18-A34)**2+(C18-C34)**2+(G18-G34)**2+(T18-T34)**2)
nucldistance1849=math.sqrt((A18-A49)**2+(C18-C49)**2+(G18-G49)**2+(T18-T49)**2)
nucldistance3449=math.sqrt((A34-A49)**2+(C34-C49)**2+(G34-G49)**2+(T34-T49)**2)
distancematrix2[0][1]=distancematrix2[1][0]=round(nucldistance0416,2)
distancematrix2[0][2]=distancematrix2[2][0]=round(nucldistance0418,2)
distancematrix2[0][3]=distancematrix2[3][0]=round(nucldistance0434,2)
distancematrix2[0][4]=distancematrix2[4][0]=round(nucldistance0449,2)
distancematrix2[1][2]=distancematrix2[2][1]=round(nucldistance1618,2)
distancematrix2[1][3]=distancematrix2[3][1]=round(nucldistance1634,2)
distancematrix2[2][3]=distancematrix2[3][2]=round(nucldistance1649,2)
distancematrix2[2][4]=distancematrix2[4][2]=round(nucldistance1849,2)
distancematrix2[3][4]=distancematrix2[4][3]=round(nucldistance3449,2)

nuclfile=open("Nucleotidedistancematrix","w")
nuclfile.write("Genome04 Genome16 Genome18 Genome34 Genome49""\n")
nuclfile.write(str(distancematrix2))
nuclfile.close()

################################################################################
### Dinucleotide frequencies
################################################################################

genome04 = np.matrix('3.83 4.70 5.21 4.75;  5.88 7.70 12.72 5.18; 7.19 11.93 7.74 4.71; 1.58 7.16 5.90 3.83')
genome16 = np.matrix('6.30 5.90 4.61 5.42;  6.84 6.40 9.85 4.63; 7.62 7.82 6.41 5.92; 1.47 7.60 6.90 6.31')
genome18 = np.matrix('9.13 4.92 5.35 6.94;  6.55 7.70 4.22 5.29; 5.43 5.75 7.72 4.89; 5.24 5.40 6.49 8.99')
genome34=np.matrix('10.72 5.39 5.87 8.82;  6.54 3.95 3.00 5.84; 6.29 3.78 3.95 5.29; 7.25 6.22 6.49 10.61')
genome49=np.matrix('1.98 4.43 6.17 2.20; 4.62 12.23 12.36 6.13; 6.58 12.05 12.05 4.45; 1.60 6.63 4.55 1.97')

#04 vs 04
subtract0404=np.subtract(genome04, genome04)
square0404=np.square(subtract0404)
number0404=square0404.sum()
distance0404=round(math.sqrt(number0404),2)
#04 vs 16
subtract0416=np.subtract(genome04, genome16)
square0416=np.square(subtract0416)
number0416=square0416.sum()
distance0416=round(math.sqrt(number0416),2)
#04 vs 18
subtract0418=np.subtract(genome04, genome18)
square0418=np.square(subtract0418)
number0418=square0418.sum()
distance0418=round(math.sqrt(number0418),2)
#04 vs 34
subtract0434=np.subtract(genome04, genome34)
square0434=np.square(subtract0434)
number0434=square0434.sum()
distance0434=round(math.sqrt(number0434),2)
#04 vs 49
subtract0449=np.subtract(genome04, genome49)
square0449=np.square(subtract0449)
number0449=square0449.sum()
distance0449=round(math.sqrt(number0449),2)
#16 vs 16
subtract1616=np.subtract(genome16, genome16)
square1616=np.square(subtract1616)
number1616=square1616.sum()
distance1616=round(math.sqrt(number1616),2)
#16 vs 18
subtract1618=np.subtract(genome16, genome18)
square1618=np.square(subtract1618)
number1618=square1618.sum()
distance1618=round(math.sqrt(number1618),2)
#16 vs 34
subtract1634=np.subtract(genome16, genome34)
square1634=np.square(subtract1634)
number1634=square1634.sum()
distance1634=round(math.sqrt(number1634),2)
#16 vs 49
subtract1649=np.subtract(genome16, genome49)
square1649=np.square(subtract1649)
number1649=square1649.sum()
distance1649=round(math.sqrt(number1649),2)
#18 vs 18
subtract1818=np.subtract(genome18, genome18)
square1818=np.square(subtract1818)
number1818=square1818.sum()
distance1818=round(math.sqrt(number1818),2)
#18 vs 34
subtract1834=np.subtract(genome18, genome34)
square1834=np.square(subtract1834)
number1834=square1834.sum()
distance1834=round(math.sqrt(number1834),2)
#18 vs 49
subtract1849=np.subtract(genome18, genome49)
square1849=np.square(subtract1849)
number1849=square1849.sum()
distance1849=round(math.sqrt(number1849),2)
#34 vs 34
subtract3434=np.subtract(genome34, genome34)
square3434=np.square(subtract3434)
number3434=square3434.sum()
distance3434=round(math.sqrt(number3434),2)
#34 vs 49
subtract3449=np.subtract(genome34, genome49)
square3449=np.square(subtract3449)
number3449=square3449.sum()
distance3449=round(math.sqrt(number3449),2)
#49 vs 49
subtract4949=np.subtract(genome49, genome49)
square4949=np.square(subtract4949)
number4949=square4949.sum()
distance4949=round(math.sqrt(number4949),2)

filedinucleotide=open('Dinucleotidedistancematrix', 'w')
DistanceMatrixDinucleotide=np.matrix([[distance0404, distance0416, distance0418, distance0434, distance0449],[distance0416, distance1616, distance1618, distance1634, distance1649],[distance0418, distance1618, distance1818, distance1834, distance1849],[distance0434, distance1634, distance1834, distance3434, distance3449],[distance0449, distance1649, distance1849, distance3449, distance4949]])
filedinucleotide.write('Genome04 Genome16 Genome18 Genome34 Genome49'+ '\n'+ str(DistanceMatrixDinucleotide))
filedinucleotide.close()
