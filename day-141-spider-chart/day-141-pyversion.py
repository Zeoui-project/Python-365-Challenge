import matplotlib.pyplot as plt
import numpy as np

#Data
categories = ['Speed', 'Power', 'Accuracy', 'Endurance', 'Agility']
player1_stats = [90, 75, 85, 80, 90]

#Number of Categories
N = len(categories)

#Create an array for the angles
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

#Initiate the plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

#Add the first player's stats to the plot
stats = player1_stats + player1_stats[:1]
ax.plot(angles, stats, linewidth=2, linestyle='solid', label='Player 1')
ax.fill(angles, stats, alpha=0.4)

#Set the labels for each axis
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

#Set the range for each axis
ax.set_ylim(0, 100)

#Add a title
plt.title('Spider Chart')

#Add a Legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

#Show the plot
plt.show()