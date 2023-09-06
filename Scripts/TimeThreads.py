"""
Mesure the performance of different numbers of threads
"""

import soapy

configFile = "./conf/OCGSSMF.yaml"
sim = soapy.Sim(configFile)

def runSim(sim: soapy.Sim, nThreads: int):
    sim.config.sim.threads = nThreads
    sim.aoinit()
    sim.makeIMat()
    sim.aoloop()
    return

runSim(sim, 1)

# Magic Method to time function
import timeit
# Number of times to run the function
n = 1
# Number of threads to test
nThreads = [1,2,4,6,7,8,9,10,11,12,14,16]
# List to store the times
times = []
# Loop over the number of threads
for n in nThreads:
    # Time the function
    t = timeit.timeit(lambda: runSim(sim, n), number=1)
    # Append the time to the list
    times.append(t)

print(times)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(nThreads, times, 'bo-')
plt.xlabel("Number of Threads")
plt.ylabel("Time (s)")
plt.title("Time to run a sim")
plt.show()