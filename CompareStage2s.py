import os
import pandas as pd
import numpy as np

direct = '/home/chintan/Desktop/'
doc = 'Stage2IDs.csv'
Outcomes = pd.read_csv(direct+doc)

Clinical = pd.Series.as_matrix(Outcomes.loc[:, 'Outcomes'])
Images = pd.Series.as_matrix(Outcomes.loc[:, 'Images'])

idx1 = pd.Index(Images) 
idx2 = pd.Index(Clinical)
Overlap = idx2.intersection(idx1)
indexes = pd.np.where(idx2.isin(Overlap))[0]

## to find indexes outsound this use:
#indexes = pd.np.where(idx2.isin(Overlap)==False)[0]

ClinImages =[]
for i in range(len(indexes)):
	ClinIDs = np.append(ClinImages, Clinical[indexes[i]])

print ClinIDs
#Params = 1 # number of returned parameters
#ClinicalImage = ClinicalImage.reshape(len(RTData)/params, params) 

#np.savetxt('Clinical.csv', ClinIDs , fmt='%s', delimiter = ',')



for i in xrange(len(indexes)):
	ID = Clinical[indexes[i]], 
	print ID
