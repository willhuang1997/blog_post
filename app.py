import matplotlib.pyplot as plt
import matplotlib.pyplot as mpld3

#create your figure and get the figure object returned
fig = plt.figure() 
plt.plot([1, 2, 3, 4, 5]) 

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
