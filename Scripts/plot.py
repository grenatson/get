import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

data = np.loadtxt("data_converted.txt")
data = data / 2 ** 8 * 3.3 #convertion from digital to analog
 
settings = np.loadtxt("settings.txt")
time_step = 1 / settings[0]
times = np.linspace(0, time_step * len(data), len(data))

fig, ax = plt.subplots()

ax.plot(times, data, linewidth=0.75, color='blue', label='V(t)')
ax.scatter(times[::int(25 / time_step)], data[::int(25 / time_step)], color='#1D60C4', alpha=1)
ax.axhline(np.max(data), lw=2, ls='--', color='green')
ax.axhline(np.min(data[int(len(data) / 2):]), lw=2, ls='--', color='green')
ax.annotate("Max voltage: {:.2f} volts".format(np.max(data)), 
            xy=(360, np.max(data)), xycoords='data',
            xytext=(10, -30), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3, angleA=0, angleB=90"),
            )
ax.annotate("Min voltage: {:.2f} volts".format(np.min(data[int(len(data) / 2):])), 
            xy=(100, np.min(data[int(len(data) / 2):])), xycoords='data',
            xytext=(20, 25), textcoords='offset points',
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="angle3, angleA=0, angleB=90"),
            )

charge_time = np.argmax(data) * time_step
discharge_time = (len(data) - 1) * time_step - charge_time
ax.text(200, 1, "Charge time: {:.0f} seconds\nDischarge time: {:.0f} seconds".format(charge_time, discharge_time), ha='center', style='italic', bbox={'boxstyle': 'round', 'alpha': 0.8, 'pad': 0.75})

ax.set_xlabel("Time [s]")
ax.set_ylabel("Voltage [V]")
ax.set_title("Charging and discharging of the capacitor in RC-circuit", fontweight='bold')
plt.minorticks_on()
ax.xaxis.set_minor_locator(MultipleLocator(25))
ax.yaxis.set_minor_locator(MultipleLocator(0.25))
ax.grid(which='major', c='0.5', lw=1)
ax.grid(which='minor', c='0.75', lw=0.5, ls='--')
ax.legend()

fig.savefig('capacitor_rc.svg')
plt.show()