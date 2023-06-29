import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 0.2
sigma = math.sqrt(variance)
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
test = stats.norm.pdf(x, mu, sigma)


def f_t(x, lam):
    t = 1 / np.sqrt(2 * np.pi * x) * np.exp(-(x + lam) / 2) * np.cosh(np.sqrt(lam * x))
    return t


t1 = np.arange(0.0, 3.0, 0.01)

fig=plt.figure(figsize=(5, 3))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

ax1.plot(x, test )
ax1.plot(x, -2 * np.log(test))

ax2.plot(x, f_t(x,0))
ax2.fill_between(x[75:100], f_t(x,0)[75:100], np.zeros(25), alpha=0.5)

ax1.set_ylim(ymin=0)
ax1.set_xticks([], minor=False)
ax1.set_yticks([], minor=False)
ax1.set_xlim([-1.25,1.25])
ax1.set_ylim([0,5])
# ax1.set_aspect('equal')
ax1.set_xlabel("$\mu$",loc="right")
ax1.legend(["$\lambda (\mu)$", "$t_\mu$", ])

ax2.set_xticks([0,x[75]])
ax2.set_xticklabels(["0","$t_{\mu,obs}$"])
ax2.set_yticks([], minor=False)
ax2.set_xlim([0,1.3])
ax2.set_ylim([0,4])
ax2.legend(["pdf($t_\mu$)=f$(t_\mu\mid \mu)$", "p-value"])
ax2.set_xlabel("$t_\mu$",loc="right")
fig.tight_layout(w_pad=3)
plt.savefig("test_stat_example.pdf")
plt.close()
