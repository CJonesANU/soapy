import numpy as np
import matplotlib.pyplot as plt

var = 1

nWalkers = int(1e7)
nSteps = 1000

finalPos = np.zeros(nWalkers)
maxPos = np.zeros(nWalkers)

for step in range(1,nSteps+1):
    stepSize = np.random.normal(0,var,nWalkers)
    newPos = finalPos + stepSize
    maxPos = np.maximum(maxPos, np.abs(newPos))
    finalPos = newPos
    print("Step: {} of {}".format(step, nSteps), end="\r")


# for walker in range(nWalkers):
#     x = 0
#     maxPos[walker] = 0
#     for step in range(nSteps):
#         x += np.random.normal(0,var)
#         maxPos[walker] = max(maxPos[walker], abs(x))
#     finalPos[walker] = x

print("Simulation Complete")
print("Final Position:")
print("Mean: {}, Var: {}".format(np.mean(finalPos), np.var(finalPos)))
print("Max Position:")
print("Mean: {}, Var: {}".format(np.mean(maxPos), np.var(maxPos)))

fig, ax = plt.subplots(1,2)
ax[0].hist(finalPos, bins=100)
ax[0].set_xlabel("Final Position")
ax[0].set_ylabel("Frequency")
ax[0].set_title("Final Position Histogram")
ax[1].hist(maxPos, bins=100)
ax[1].set_xlabel("Max Position")
ax[1].set_ylabel("Frequency")
ax[1].set_title("Max Position Histogram")
plt.show()
