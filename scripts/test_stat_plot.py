import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

mu = 0
variance = 0.2
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
test = stats.norm.pdf(x, mu, sigma)
plt.plot(x, test*7)
plt.plot(x, -2*np.log(test))
plt.plot(x, test*4)
# plt.text(x=-1,y=1,s="this is a sketch!",color="r",fontsize=15)
plt.fill_between(x[75:100], test[75:100]*4,np.zeros(25),alpha=0.5)
plt.legend(["$\lambda (\mu)$","$t_\mu$", "pdf($t_\mu$)=f$(t_\mu\mid \mu)$","p-value"])

ax=plt.gca()
ax.set_xticks([x[75]])
ax.set_xticklabels(['$t_\mu$,obs'])
ax.set_ylim(ymin=0)
plt.yticks([], [])
plt.savefig("test_stat_example.pdf")
plt.close()