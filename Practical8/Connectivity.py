import collections
filehandle=open('04ExtractedNetwork', 'r')
text=filehandle.read().splitlines()
filehandle.close()

dict1=collections.OrderedDict()
#countervalues=0
for lines in text:
    line=lines.split(' ')
    if line[0] not in dict1.keys():
        dict1[line[0]]=[line[1]]
 #       countervalues=countervalues+1
    elif line[0] in dict1.keys():
        dict1[line[0]].append(line[1])
  #      countervalues=countervalues+1
        
proteins=len(dict1.keys())
#print (proteins)
interactions=len(text)
#print(countervalues, interactions)
AverageConnectivity=interactions/proteins
print ('The average connectivity for Bradyrhizobium japonicum interactome is ' + str(AverageConnectivity))

NodeDegree=[]
for key, value in dict1.items():
    NodeDegree.append(len([item for item in value if item])) #Get number of values per key


import matplotlib.pyplot as plt
import numpy as np

NodeDegreeLog=np.log10(NodeDegree)

#HISTOGRAM PLOTS
CombinedPlot=plt.figure()
plot1=CombinedPlot.add_subplot(221)
n1, bins1, patches1 = plot1.hist(NodeDegree, bins=25)

plot2=CombinedPlot.add_subplot(223)
plot2.set_yscale('log')
n2, bins2, patches2 = plot2.hist(NodeDegreeLog, log=True, bins=25) #n is the count in each bin and bins are the edges of the bin

#SCATTERPLOTS
plot3=CombinedPlot.add_subplot(222)
meanvaluebin1 = [0.5 * (bins1[i] + bins1[i+1]) for i in range(len(n1))]
plot3.scatter(meanvaluebin1, n1)

plot4=CombinedPlot.add_subplot(224)
meanvaluebin2 = [0.5 * (bins2[i] + bins2[i+1]) for i in range(len(n2))]
plot4.scatter(meanvaluebin2, np.log10(n2))

plot1.set_xlabel('Node Degree')
plot2.set_xlabel('Node Degree (log scale)')
plot3.set_xlabel('Node Degree')
#plot3.set_xlim([0,3000])
#plot3.set_ylim([-50,2500])
plot4.set_xlabel('Node Degree (log scale)')
plot1.set_ylabel('Frequency')
plot2.set_ylabel('Frequency (log scale)')
plot3.set_ylabel('Frequency')
plot4.set_ylabel('Frequency (log scale)')
#plot4.set_xlim([-0.5,3.5])
plt.show()





