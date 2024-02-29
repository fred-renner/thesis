import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, poisson
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Define the Gaussian and Poissonian functions
def gaussian(x, a):
    return norm.pdf(x, loc=0, scale=1/a)

def poissonian(k, lam):
    return poisson.pmf(k, lam)

def Z(a, x, k=20):
    return gaussian(x, a) * poissonian(k, a)

# Initial parameter a
a0 = 1

# Gaussian plot
x = np.linspace(-10, 10, 400)
fig, axs = plt.subplots(2, figsize=(10, 8))
axs[0].plot(x, gaussian(x, a0), label='Gaussian')
gaussian_dot, = axs[0].plot([0], gaussian(0, a0), 'ro')

# Poissonian plot
k = 20
lam = a0
poisson_x = np.arange(poisson.ppf(0.01, lam), poisson.ppf(0.99, lam))
axs[1].stem(poisson_x, poissonian(poisson_x, lam), label='Poissonian', basefmt=" ")
poissonian_dot, = axs[1].plot([k], poissonian(k, lam), 'ro')

# Slider for parameter 'a'
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor=axcolor)
slider_a = Slider(ax_a, 'Parameter a', 0.1, 5.0, valinit=a0)

# Update function for the slider
def update(val):
    a = slider_a.val
    gaussian_dot.set_ydata(gaussian(0, a))
    poissonian_dot.set_ydata(poissonian(k, a))
    axs[0].set_ylim(0, max(gaussian(x, a)) + 0.05)
    axs[1].set_ylim(0, max(poissonian(poisson_x, a)) + 0.05)
    fig.canvas.draw_idle()

slider_a.on_changed(update)

# 3D plot for Z
fig_3d = plt.figure(figsize=(10, 8))
ax_3d = fig_3d.add_subplot(111, projection='3d')
X, A = np.meshgrid(x, np.linspace(0.1, 5, 30))
Z_vals = Z(A, X)
ax_3d.plot_surface(X, A, Z_vals, cmap='viridis', alpha=0.7)
Z_dot = ax_3d.scatter([0], [a0], [Z(a0, 0)], color='r')

def update_3d(val):
    a = slider_a.val
    Z_dot._offsets3d = ([0], [a], [Z(a, 0)])
    fig_3d.canvas.draw_idle()

slider_a.on_changed(update_3d)

plt.show()

