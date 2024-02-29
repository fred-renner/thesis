import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
import json

# Creating a figure and an axis
fig, ax = plt.subplots(figsize=(5, 4))

with open(
    "/Users/fred/phd/thesis/scripts/LimitScan_k2V_parameterized_BDT_decorXbb.json"
) as f:
    rel21 = json.load(f)

xsec = 27.113741
values = np.array(
    [
        [rel21["-2"][5] * xsec, 3.38],
        [rel21["-1"][5] * xsec, 5.56],
        [rel21["0"][5] * xsec, 10.43],
        [rel21["1"][5] * xsec, 22.32],
        [rel21["2"][5] * xsec, 49.93],
    ]
).T

# xbb 60

# labels = [r"$m_{HH}$", "classic nn", "neos"]
# values = (
#     np.array(
#         [
#             [0.3128, 0.2450, 0.1061],
#             [0.4866, 0.3811, 0.1706],
#             [0.8580, 0.6695, 0.3269],
#             [1.7200, 1.3382, 0.7210],
#             [3.6412, 2.8364, 1.7124],
#         ]
#     ).T
#     * xsec
# )


# xbb 70

labels = [
    "3_m_hh",
    "3_bce",
    "3_neos_stripped",
    "3_neos_sys",
    "3_neos_bins",
    "3_neos_sys_bins",
    "3_neos_sys_bins_stat",
    "4_neos_sys_bins_stat",
    "5_neos_sys_bins_stat",
]
values = (
    np.array(
        [
            [0.4001, 0.2402, 0.1162, 0.1234, 0, 0.1473, 0.2343, 0.2306, 0.2556],
            [0.6190, 0.3620, 0.1899, 0.1997, 0, 0.2352, 0.3581, 0.3534, 0.3905],
            [1.0853, 0.6307, 0.3671, 0.3735, 0, 0.4293, 0.6177, 0.6128, 0.6738],
            [2.1459, 1.2439, 0.8293, 0.8219, 0, 0.8958, 1.2196, 1.2166, 1.3200],
            [4.4515, 2.6067, 2.0923, 1.9344, 0, 2.0146, 2.5534, 2.5634, 2.7389],
        ]
    ).T
    * xsec
)

# Plot and fill between the lines

for i, y in enumerate(values):
    x = np.linspace(i, i + 1, 10)
    ax.fill_between(x, y[0], y[1], color="gold")
    ax.fill_between(x, y[1], y[2], color="limegreen")
    ax.hlines(y[2], x[0], x[-1], color="black")
    ax.fill_between(x, y[2], y[3], color="limegreen")
    ax.fill_between(x, y[3], y[4], color="gold")


ax.legend(
    [
        r"expected Limit $\pm 2\sigma$",
        r"expected Limit $\pm 1\sigma$",
        r"expected Limit",
    ],
    fontsize="large",
    loc="upper right",
)
plt.ylabel(r"95 % CL limit on $\sigma_{\kappa_{2v}=0}$ [fb]")
plt.xticks(
    np.arange(0.5, len(labels), step=1), labels
)  # Setting x-axis ticks in integer steps from 0 to 10
plt.xticks(rotation=45, ha="right")
plt.ylim([0, 120])
ax.yaxis.set_minor_locator(MultipleLocator(5))
plt.yticks(minor=True)
plt.grid(alpha=0.35, which="both", color="grey")
plt.tight_layout()
plt.savefig("brazil_limits.pdf")
