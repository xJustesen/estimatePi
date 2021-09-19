from src.MCEstimator import MCEstimator
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    estimator = MCEstimator()
    pi = estimator.pi()
    x = estimator.x_samples
    y = estimator.y_samples
    theta = np.linspace(0, np.pi / 2)

    fig, ax = plt.subplots()
    ax.scatter(x, y, color='k', zorder=1, s=0.01)
    ax.plot(np.cos(theta), np.sin(theta), 'r--', lw=1)
    ax.set_title(f'PI Estimate = {pi}')
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_aspect('equal', adjustable='box')
    plt.show()