

import matplotlib.pyplot as plt
import numpy as np


def update_ax2(axx):
    ax2.set_ylim(0, 100)
    ax2.figure.canvas.draw()


# the data to plot
defects = [32, 22, 15, 5, 2]
labels = ['vertical', 'horizontal', 'behind', 'left area', 'other']
the_sum = sum(defects)  # ie, 32 + 22 + 15 + 5 + 2
the_cumsum = np.cumsum(defects)  # 32, 32 + 22, 32 + 22 + 15, 32 + 22 + 15 + 5, 32 + 22, + 15 + 5 + 2
ind = np.arange(len(defects))  # the x locations for the groups
width = .98  # with do of the bars, where a width of 1 indidcates no space between bars
x = ind + .5 * width  # find the middle of the bar
fig = plt.figure()  # create a figure
ax1 = fig.add_subplot(111)  # and a subplot
ax2 = ax1.twinx()  # create a duplicate y axis
# create the callback to automatically update the y axis
ax1.callbacks.connect("ylim_changed", update_ax2)
# create an upper limit for the y axis.
# The upper limit is the sum of all the numbers
ax1.set_ylim(ymax=the_sum)
rects1 = ax1.bar(ind, defects, width=width)  # draw the chart
line, = ax1.plot(x, the_cumsum)  # draw the  line
ax1.set_xticks(ind + .5 * width)  # set ticks for middle of bars
ax1.set_xticklabels(labels)  # create the labels for the bars
ax1.set_ylabel('Defects')  # create the left y axis label
ax2.set_ylabel('Percentage')  # create the right y axis label
plt.show()
