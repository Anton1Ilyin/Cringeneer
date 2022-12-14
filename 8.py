import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


settings=np.loadtxt("settings.txt", dtype=float)
data=np.loadtxt('data.txt', dtype=int) * settings[1]
data_time=np.array([i*1/settings[0] for i in range(data.size)])


fig, ax=plt.subplots(figsize=(8, 5), dpi=150)


ax.plot(data_time, data, c='black', linestyle='solid', linewidth=1, label = f'$V(t)$')
ax.scatter(data_time[0:data.size:100], data[0:data.size:100], marker = 'D', c = 'red', s=10)
ax.legend(shadow = False, loc = 'upper right', fontsize = 10)


ax.set_xlim(left=min(data_time), right=max(data_time)+1)
ax.set_ylim(bottom=min(data), top=max(data)+0.2)


ax.xaxis.set_major_locator(ticker.MultipleLocator(2*3))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5*3))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5*3))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1*3))



ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = '--')



ax.set_title('Процесс заряда и разряда конденсатора в RC цепи')
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")


plt.show()

fig.savefig('graphic.png')
fig.savefig('graphic.svg')
