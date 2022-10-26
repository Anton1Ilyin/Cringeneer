import matplotlib.pyplot as plt
import numpy as np
data_array=np.loadtxt("data.txt", dtype=int)
settings_array=np.loadtxt("settings.txt", dtype=float)
fig, ax =plt.subplots(figsize=(16, 10), dpi=400)
ax.plot([float(t/settings_array[1]) for t in range(len(data_array))] ,data_array*settings_array[0], linewidth=1.5, color='red', linestyle='solid')
ax.scatter([float(t/settings_array[1]) for t in range(0,len(data_array),1000)] ,data_array[::1000]*settings_array[0], )
ax.grid()
#ax.legend()
ax.set_ylabel('Напряжение [B]')
ax.set_xlabel('Время [сек]')
ax.set_title('График напряжения')
ax.set_xlim(left =0, right=103)
ax.set_ylim(bottom=0, top=3.3)


#fig.savefig("plot.svg")
plt.show()
