import os
import pandas as pd
import numpy as np

direct = '/home/chintan/Desktop/PhaseIITrials/'
doc = '3DClinicalOutcomes.csv'
Outcomes = pd.read_csv(direct+doc)

PID = pd.Series.as_matrix(Outcomes.loc[:, 'PID']) 
Surv2 = pd.Series.as_matrix(Outcomes.loc[:, 'SURV2'])
Days = pd.Series.as_matrix(Outcomes.loc[:, 'Days'])
Stage = pd.Series.as_matrix(Outcomes.loc[:, 'Stage'])
Pred = pd.Series.as_matrix(Outcomes.loc[:, '3DPredictions']) 

T = np.linspace(0,24, Surv2.shape[0])
E = Surv2
g = Pred
g[g>=median(g)+0.01] = 1
g[g<median(g)_0.01] = 0

#g[g>= 0.95] = 1
#g[g< 0.95] = 0


from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()
kmf.fit(T, event_observed=E)  # or, more succiently, kmf.fit(T, E)

#plt.figure()
kmf.survival_function_
kmf.median_
kmf.plot()

groups = g
ix = (groups == 0)

#plt.figure()
kmf.fit(T[~ix], E[~ix], label='Low risk')
ax = kmf.plot()

kmf.fit(T[ix], E[ix], label='High risk')
kmf.plot(ax=ax)
plt.xlabel('Months elapsed')
plt.ylabel('Survivorship')
plt.title('KM Plot from Model Predictions')

from lifelines.statistics import logrank_test

results = logrank_test(T[ix], T[~ix], E[ix], E[~ix], alpha=.95)
print results


