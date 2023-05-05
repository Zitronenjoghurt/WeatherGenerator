# This is for testing mean and deviation to check different probability curves

import random
from matplotlib import pyplot as plt

a = -10
b = 15
mean = -8
deviation = 7
num_samples = 1000000

samples = []
for i in range(num_samples):
    x = random.gauss(mean, deviation)
    while x < a or x > b:  # make sure the result is within the given interval
        x = random.gauss(mean, deviation)
    samples.append(x)

plt.hist(samples, bins=50)
plt.show()