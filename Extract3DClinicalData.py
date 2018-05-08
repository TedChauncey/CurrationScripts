# Script find patient IDs in 3D images and pulls outcome for them

import os
import pandas as pd
import numpy as np

direct = '/home/chintan/Desktop/PhaseIITrials/'
doc = 'Stage2SurvivalData.csv'
Outcomes = pd.read_csv(direct+doc)

PID = pd.Series.as_matrix(Outcomes.loc[:, 'PID']) 
Images = pd.Series.as_matrix(Outcomes.loc[:, '3DImages'])
SURV2 = pd.Series.as_matrix(Outcomes.loc[:, 'SURV2'])
Days = pd.Series.as_matrix(Outcomes.loc[:, 'Days_Diff'])
Stage = pd.Series.as_matrix(Outcomes.loc[:, 'CSTAGE'])
Histology = pd.Series.as_matrix(Outcomes.loc[:, 'CTYPE']) 


idx1 = pd.Index(Images) 
idx2 = pd.Index(PID)
Overlap = idx2.intersection(idx1)
indexes = pd.np.where(idx2.isin(Overlap))[0]


for i in xrange(len(indexes)):
	NewOutcomes = [PID[indexes[i]], SURV2[indexes[i]], Days[indexes[i]], Stage[indexes[i]], Histology[indexes[i]] ]
	print NewOutcomes
	
# find the images that are excluded

ImageLeft = np.setdiff1d(idx1,idx2)
print ImageLeft
