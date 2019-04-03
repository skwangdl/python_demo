import numpy as np
import matplotlib.pyplot as plt

# Hello Python Data Analysis
# 产生标准正态分布的随机数，绘图展示

mu = 1
sigma = 3
num = 100000

rand_data = np.random.normal(mu, sigma, num)
count, bins, ignored = plt.hist(rand_data, 30)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(bins - mu) ** 2/(2*sigma**2)), linewidth=2, color='r')
plt.show()
