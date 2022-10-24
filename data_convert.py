import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.txt")
data_converted = data * 2 ** 8 / 3.3
np.savetxt('data_converted.txt', data_converted, delimiter='/n', fmt='%d')

frequency, v_step = np.loadtxt("settings.txt")
np.savetxt("settings.txt", [frequency, 3.3 / 2 ** 8], delimiter='/n', fmt='%f')

'''
measures = range(1, len(data_converted) + 1)
figure, axs = plt.subplots(2)

axs[0].plot(measures, data_converted)
axs[0].set_xlabel('N')
axs[0].set_ylabel('digital voltage')

axs[1].plot(measures, data)
axs[1].set_xlabel('N')
axs[1].set_ylabel('voltage')

plt.show()
'''