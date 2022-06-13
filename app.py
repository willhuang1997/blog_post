import streamlit as st
import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd
import streamlit.components.v1 as components

fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

N = 50
df = pd.DataFrame(index=range(N))
df['x'] = np.random.randn(N)
df['y'] = np.random.randn(N)
df['z'] = np.random.randn(N)

points = ax.plot(df.x, df.y, 'o', color='b',
                 mec='k', ms=15, mew=1, alpha=.6)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Demo Graph!', size=20)
fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
