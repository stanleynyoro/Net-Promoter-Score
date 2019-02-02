import pandas as pd
import numpy as np
Interval=[1,2,3,4,5,6,7,8,9,10]
A=np.random.choice(Interval,387,p=[0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.35,0.2])
B=np.random.choice(Interval,387,p=[0.02,0.01,0.02,0.05,0.15,0.05,0.05,0.15,0.3,0.2])
C=np.random.choice(Interval,387,p=[0.05,0.01,0.05,0.02,0.05,0.1,0.1,0.1,0.3,0.22])
Data=pd.DataFrame({'Company A':A,'Company B':B,'Company C':C})

lower_score_A=[]
upper_score_A=[]
for i in Data['Company A']:
    if(i<=6):
        lower_score_A.append(i)
    elif(i>8):
        upper_score_A.append(i)
        n_lower_A=len(lower_score_A)/len(Data['Company A'])
        n_upper_A=len(upper_score_A)/len(Data['Company A'])
        nps_A=round((n_upper_A-n_lower_A),2)
############################
lower_score_B=[]
upper_score_B=[]
for j in Data['Company B']:
    if(j<=6):
        lower_score_B.append(j)
    elif(j>8):
        upper_score_B.append(j)
        n_lower_B=len(lower_score_B)/len(Data['Company B'])
        n_upper_B=len(upper_score_B)/len(Data['Company B'])
        nps_B=round((n_upper_B-n_lower_B),2)

############################
lower_score_C=[]
upper_score_C=[]

for k in Data['Company C']:
    if(k<=6):
        lower_score_C.append(k)
    elif(k>8):
        upper_score_C.append(k)
        n_lower_C=len(lower_score_C)/len(Data['Company C'])
        n_upper_C=len(upper_score_C)/len(Data['Company C'])
        nps_C=round((n_upper_C-n_lower_C),2)
        
print('NPS for: A is {0}, for B is {1}, for is C {2}'.format(nps_A,nps_B,nps_C))
