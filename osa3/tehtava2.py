from matplotlib import pyplot as plt, patches
import numpy as np

# Set the figure size to 6.4 x 4.8 inches and extend the width
plt.figure(figsize=(19.2, 4.8))
ax = plt.subplot()

# Draw the unit circle
circle = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(circle)

# Move left y-axis and bottom x-axis to the center
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks on the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Set axis to be equal
ax.axis('equal')

# Set the angles in degrees and convert to radians
angles_deg = [30, 45, 60, 90, 120, 150, 180, 270]
angles_rad = np.radians(angles_deg)

# Calculate coordinates on the unit circle
x = np.cos(angles_rad)
y = np.sin(angles_rad)

# Define labels, colors, and line styles for each angle
labels = [r'$\frac{\pi}{6}$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$',
          r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$', r'$\frac{3\pi}{2}$']
colors = ['orange', 'purple', 'brown', 'red', 'green', 'blue', 'cyan', 'magenta']
line_styles = ['-', '--', '-.', ':', '-', '--', '-.', ':']

# Extend x-axis range from -3π to 3π
x_range = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
y_range = np.sin(x_range)  # You can plot sine or cosine here based on your needs

# Plot each point and label on the unit circle
for i, (xi, yi) in enumerate(zip(x, y)):
    plt.scatter(xi, yi, color=colors[i], marker='X', label=labels[i])
    plt.annotate(labels[i],
                 xy=(xi, yi), xycoords='data',
                 xytext=(+10, +10), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

# Plot sine curve with new style
plt.plot(x_range, np.sin(x_range), color='black', linestyle='-', label='sin(x)')

# Add legend
plt.legend()

# Set ticks for x and y axis
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

# Show the plot
plt.show()