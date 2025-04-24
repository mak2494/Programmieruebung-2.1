import matplotlib.pyplot as plt
import numpy as np
from load_data import load_data
from sort import bubble_sort

data = load_data('activity.csv')
power_W = data['PowerOriginal']
sorted_power_W = bubble_sort(power_W)

# Data for plotting
N_steps=(len(power_W))
t = np.arange(0, N_steps, 1)
p = sorted_power_W[::-1]

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(t, p, color='pink')

ax.set(xlabel='time in seconds', ylabel='Power in Watts',
       title='Power Curve')
ax.set_xticks(np.arange(0, len(t), 100))  

fig.savefig("figures\Power_Curve.png")
ax.grid()
plt.show()