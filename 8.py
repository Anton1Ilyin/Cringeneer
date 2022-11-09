import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

data_array=np.loadtxt("data.txt", dtype=int)
settings_array=np.loadtxt("settings.txt", dtype=float)

fig, ax =plt.subplots(figsize=(16, 10), dpi=400)

ax.plot([float(t/settings_array[1]) for t in range(len(data_array))] ,data_array*settings_array[0], linewidth=1.5, color='red', linestyle='solid', label=f'$V(t)$')
ax.scatter([float(t/settings_array[1]) for t in range(0,len(data_array),1000)] ,data_array[::1000]*settings_array[0], marker='h', color='red', s=10)

ax.grid(which='major', color = 'black')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

ax.legend(loc = 'upper right', fontsize = 20)

#plt.text(6.2*10**10, 2.55, f'Время разрядки')


ax.set_ylabel('Напряжение [B]')
ax.set_xlabel('Время [сек]')
ax.set_title('График напряжения')

ax.set_xlim(left=0, right=103)
ax.set_ylim(bottom=0, top=3.3)


#fig.savefig("plot.svg")
plt.show()
