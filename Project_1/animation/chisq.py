import numpy as np
from scipy.stats import chi2
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
plt.figure(figsize = (8, 6))
fig = plt.gcf()
ax = plt.gca()

xlim = [0, 50]
x = np.linspace(xlim[0], xlim[1], 1000)
dfs = np.arange(4, 32, 1)

colors = plt.colormaps['Blues'](np.linspace(0.5, 1, len(dfs)))

plt.axis([xlim[0], xlim[1], 0, 0.21])

for df, color in zip(dfs, colors):
    y = chi2.pdf(x, df)
    line, = plt.plot(x, y, lw = 1.5, color = color, label = r'$\nu$ = {}'.format(df))
    plt.xlabel('$D.F.$', fontsize = 15, color = 'black', fontweight = 'bold')
    plt.ylabel('Density', fontsize = 15, color = 'black', fontweight = 'bold')

    ax.legend([line], [line.get_label()], loc = 'upper right')

    plt.tick_params(axis = 'both', colors = 'black')
    plt.title('$\chi^2$ Distributions', fontsize = 18, fontweight='bold')
    plt.yticks([0, 0.1, 0.2])
    plt.tight_layout()
    plt.pause(0.5)

    if ax.get_legend() is not None:
        ax.get_legend().remove()

plt.text(30, 0.15, r'${} \leq d.f. \leq {}$'.format(dfs[0], dfs[-1]), fontsize = 18, color = 'k', 
         ha = 'center')
plt.show()