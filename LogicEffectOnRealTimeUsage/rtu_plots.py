import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("rtu_data.csv",delimiter=",",na_values="Nan")

#plt.clf()
fig, ax = plt.subplots(3, 1, sharex='col')

ax[0].scatter(data["ops"][:-1],data["mn"][:-1])
ax[0].set(
    title="Minimum Operation time vs. operation count",
    ylabel="time us")
ax[1].scatter(data["ops"][:-1],data["mx"][:-1])
ax[1].set(
    title="Maximum Operation time vs. operation count",
    ylabel="time us")
ax[2].scatter(data["ops"][:-1],data["exc"][:-1])
ax[2].set(
    title="Exceed counts vs. operation count",
    ylabel="exception qty")
plt.show()
