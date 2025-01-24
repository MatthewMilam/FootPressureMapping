# Main python file for reading data from csv file and displaying foot pressures.

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Example forces for each frame
forces = [20, 40, 60, 80, 100]  # Replace with your desired force values

# Function to update the colors of the circles for animation
# force is an np row (all values 0-100)
def update(force, heel_circle_L, left_circle_L, right_circle_L, heel_circle_R, left_circle_R, right_circle_R):
    # viridis 
    heel_circle_L.set_facecolor(plt.cm.viridis(force / 100))
    left_circle_L.set_facecolor(plt.cm.viridis(force / 100))
    right_circle_L.set_facecolor(plt.cm.viridis(force / 100))
    heel_circle_R.set_facecolor(plt.cm.viridis(force / 100))
    left_circle_R.set_facecolor(plt.cm.viridis(force / 100))
    right_circle_R.set_facecolor(plt.cm.viridis(force / 100))
    return heel_circle_L, left_circle_L, right_circle_L, heel_circle_R, left_circle_R, right_circle_R

def plot_foot(ax, side='left'):
    foot_outline = np.array([
        [2,0], [3,0], [4,2], [5,8], [5,10], [1,10], [0,9], [0,2], [2,0]
    ])

    # Adjust values for right foot.
    if side == 'right':
        foot_outline[:, 0] += 2 * (6 - foot_outline[:, 0])

    # Plot the foot outline
    ax.plot(foot_outline[:, 0], foot_outline[:, 1], color='black')

    # left side circles
    heel_pos = [2.3, 1.5]
    left_pos = [1, 8]
    right_pos = [4, 9]
    
    # Reflect over axis if right foot:
    if side == 'right':
        heel_pos[0] += 2 * (6 - heel_pos[0])
        left_pos[0] += 2 * (6 - left_pos[0])
        right_pos[0] += 2 * (6 - right_pos[0])


    # Create the circles
    heel_circle = plt.Circle(heel_pos, radius=0.5, color='black', alpha=0.5)
    left_circle = plt.Circle(left_pos, radius=0.5, color='black', alpha=0.5)
    right_circle = plt.Circle(right_pos, radius=0.5, color='black', alpha=0.5)

    # Add the circles to the plot
    ax.add_patch(heel_circle)
    ax.add_patch(left_circle)
    ax.add_patch(right_circle)

    return heel_circle, left_circle, right_circle

df = pd.read_csv('Test_Data_1.csv')

# DataFrame structure is first half dataframe is left foot, right half is right foot.
# Currently with 3 sensors per foot, it is bottom, outer, inner

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the left foot and right foot
heel_circle_L, left_circle_L, right_circle_L = plot_foot(ax, 'left')
heel_circle_R, left_circle_R, right_circle_R = plot_foot(ax, 'right')


# Size of the grid (needs to show all of feet)
ax.set_xlim(-1, 13)
ax.set_ylim(-1, 12)
ax.set_aspect('equal')

ax.grid(True)

# Remove axes for clarity
ax.axis('off')

# Create the animation
# frames=forces means there will be 5 frames (forces array is size 5) and the input for update is forces[i]
ani = FuncAnimation(fig, update, frames=forces, fargs=(heel_circle_L, left_circle_L, right_circle_L, heel_circle_R, left_circle_R, right_circle_R), interval=1000, blit=True)

# TODO: adjust above funcAnimation. update function will instead take a 1d array as input.
# So, the overall data will be a 2d array of size 6x(numFrames), so 6x50.

# Display the plot
plt.show()

