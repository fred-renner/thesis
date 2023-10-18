import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 18})
import math

x = np.linspace(1e-20, 1e-17, 100)


def f(x):
    alpha_0 = 1 / 137
    result = alpha_0 / (1 - (alpha_0 * (1 / (3 * math.pi) * np.log(x ))))
    return result


fig = plt.figure(figsize=(5, 3))
ax = fig.gca()
# ax.set_xlim([0,1.3])
# ax.set_ylim([0,4])
# ax.legend(["pdf($t_\mu$)=f$(t_\mu\mid \mu)$", "p-value"])
plt.plot(x, f(x))
ax.set_xlabel(r"$q^2$")
ax.set_ylabel(r"$\alpha(q^2)$")
ax.set_xticks([], minor=False)
ax.set_yticks([], minor=False)
# ax.set_xscale('log')
fig.tight_layout()
plt.savefig("simple_function.pdf")
plt.close()
