from src.MCEstimator import MCEstimator
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


np.random.seed(314)
NSAMPLES = int(1.5e4)
COORDS = np.random.random_sample((NSAMPLES, 2))

@st.cache(suppress_st_warning=True)
def get_samples(stop):
    if stop > NSAMPLES:
        raise ValueError
    return COORDS[:stop, :]


def plot_samples(ax, x, y):
    ax.scatter(x, y, color='k', zorder=1, s=0.01)


def set_plot_title(ax, title):
    ax.set_title(title)


def create_figure():
    fig, ax = plt.subplots()
    theta = np.linspace(0, np.pi/2)
    x = np.cos(theta)
    y = np.sin(theta)
    ax.plot(x, y, 'r--', lw=1)
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_aspect('equal', adjustable='box')
    return fig, ax


st.title("Let's estimate PI!")
n_samples = st.slider(
    'Select the number of samples:',
    min_value=1,
    max_value=NSAMPLES-1,
    value=1,
    step=10
)

samples = get_samples(n_samples)
estimator = MCEstimator(samples)
pi = estimator.pi()

fig, ax = create_figure()
plot_samples(ax, samples[:, 0], samples[:, 1])
title = f'PI Estimate = {pi}'
set_plot_title(ax, title)
st.pyplot(fig)
