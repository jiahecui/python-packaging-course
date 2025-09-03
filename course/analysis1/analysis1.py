# analysis1/analysis1.py
import numpy as np
import matplotlib.pyplot as plt
import tstools

timeseries = np.genfromtxt("./course/analysis1/data/brownian.csv", delimiter=",")

mean, var = tstools.get_mean_and_var(timeseries)
print(f"Mean: {mean}, variance: {var}")

fig, ax = tstools.plot_histogram(timeseries, nbins=100)