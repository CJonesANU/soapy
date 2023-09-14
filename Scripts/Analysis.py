'''
Analysis.py
'''

import pandas as pd
import matplotlib.pyplot as plt

#import datafame from csv
path = "/home/cameron/Documents/projects/soapy_TTEModule/soapy/Results.csv"
df = pd.read_csv(path)

print(df.head())

# Display each col in seperate histogram
nBins = 20
fig, ax = plt.subplots(1,5)
ax[0].hist(df["stdTT"], bins=nBins)
ax[0].set_title("stdTT")
ax[1].hist(df["maxTT"], bins=nBins)
ax[1].set_title("maxTT")
ax[2].hist(df["stdWfs"], bins=nBins)
ax[2].set_title("stdWfs")
ax[3].hist(df["maxWfs"], bins=nBins)
ax[3].set_title("maxWfs")
ax[4].hist(df["encircledArea"], bins=nBins)
ax[4].set_title("encircledArea")
# Add labels to figure
fig.suptitle("Histograms of Results")
fig.text(0.5, 0.04, ' $r_0$ = 0.1, $\sigma_{FSM}=100$, $f_{FSM}=100$; $\sigma_{tel}=50$, $f_{tel} = 15$\n maxTTStroke=1.5', ha='center')
# Annotate each subplot with mean and std
means = df.mean()[1:]
# remove first element
stds = df.std()[1:]
print(means)
print(stds)

for i in range(5):
    ax[i].annotate("Mean: {:.2f}\nStd: {:.2f}".format(means[i], stds[i]), xy=(0.6, 0.7), xycoords='axes fraction')
plt.show()
