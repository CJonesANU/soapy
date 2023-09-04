''' 
Open and analyse the data saved in Results.csv and generated by TelVarFSMResponse.pyplot
'''
import pandas as pd
import matplotlib.pyplot as plt
path = "TelVarianceResults.csv"

Results = pd.read_csv(path, index_col=0)

print(Results.head())

fig, ax = plt.subplots(2,2)
ax[0,0].plot(Results.index, Results["stdTT"],'bo-')
ax[0,0].set_title(" Std TT Magnitude")
ax[0,0].set_ylabel("Variance")

ax[0,1].plot(Results.index, Results["longStrehl"],'bo-')
ax[0,1].set_title("Long Term Strehl")
ax[0,1].set_ylabel("Strehl")


ax[1,0].plot(Results.index, Results["maxTT"],'bo-')
ax[1,0].set_title("max TT")
ax[1,0].set_ylabel("Magnitude")

# Encircled Area
ax[1,1].plot(Results.index, Results["encircledArea"],'bo-')
ax[1,1].set_title("Encircled Area")
ax[1,1].set_ylabel("Area")

# ax[1,1].plot(Results.index, Results["maxWfs"],'bo-')
# ax[1,1].set_title("wfs Max")
# ax[1,1].set_ylabel("Magnitude")


# Add Title to the figure
fig.suptitle("Variance Of Telescope")
# add author and date
fig.text(0.5, 0.01, "Author: Cameron Jones", ha='center')
fig.text(0.5, 0.04, "Date: 30/08/2023", ha='center')
fig.text(0.7, 0.01, "Maximum TT \n Stroke: 1.2")

plt.show()

