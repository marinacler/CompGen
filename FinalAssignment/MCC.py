#MCC
import math

TP=0.6
TN=0.3
FP=0.05
FN=0.05

MCC=((TP*TN)-(FN*FP))/(math.sqrt((TP+FN)*(TN+FP)*(TP+FP)*(TN+FN)))
print(round(MCC,2))
