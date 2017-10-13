import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("network_data.csv",delimiter=",")

#plt.clf()
fig, ax = plt.subplots(2, 1, sharex='col')



network, n_cov = np.polyfit(
    data["qty"],
    data["Monitored  Network traffic (MBPS+/-1)"],
    deg=1,
    cov=True)

cpu, c_cov = np.polyfit(
    data["qty"],
    data["CPU time (us+/15)"],
    deg=1,
    cov=True)

total, t_cov = np.polyfit(
    data["qty"],
    data["Total time (us+/-5)"],
    deg=1,
    cov=True)
print("network: ", network, np.sqrt(np.diag(n_cov)))
print("cpu:     ", cpu, np.sqrt(np.diag(c_cov)))
print("total:   ", total, np.sqrt(np.diag(t_cov)))

ax[0].set(
    title="System load vs. variables monitored",
    ylabel="network load (MBPS)")
ax[0].scatter(data["qty"], data["Monitored  Network traffic (MBPS+/-1)"])
ax[0].plot(data["qty"],np.poly1d(network)(data["qty"]))
ax[1].set(
    ylabel="Process time (us)",
    xlabel="Qty. variables observed")
ax[1].scatter(data["qty"], data["CPU time (us+/15)"],label="CPU")
ax[1].plot(data["qty"],np.poly1d(cpu)(data["qty"]))
ax[1].scatter(data["qty"], data["Total time (us+/-5)"],label="Total")
ax[1].plot(data["qty"],np.poly1d(total)(data["qty"]))
ax[1].legend(loc="lower right",frameon=False)
plt.show()
