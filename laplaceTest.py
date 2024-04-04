
import math
import numpy as np
import matplotlib.pyplot as plt
import reliability

data = np.genfromtxt('failure-data-set2/Failure_Data_Set/Failure_Count/CDS.csv', delimiter=',', skip_header=1)

results = np.genfromtxt('model_results.csv', delimiter=',', skip_header=1)

# col1 is for the raw data
col1 = np.array(data[:, 1])
col1 = col1.astype(int)
col1 = np.cumsum(col1)
print("Raw Data")
reliability.Repairable_systems.ROCOF(failure_times=list(col1), label='Raw')

print("\nDiscrete Weibull Type III")

dw3 = np.array(results[:, 1])
reliability.Repairable_systems.ROCOF(failure_times=list(dw3), label='DW3')

print("\nTruncated Logistic")

tl = np.array(results[:, 2])
reliability.Repairable_systems.ROCOF(failure_times=list(tl), label='TL')


plt.show()