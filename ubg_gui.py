import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
import numpy as np

class RBS:
    instances = []
    selected_instance = None

    def __init__(self, ax, x, y, sector_angle=60):
        self.ax = ax
        self.dot_radius = 0.5
        self.sector_radius = self.dot_radius + 0.3  # Initial size of the sector
        self.sector_angle = sector_angle
        self.dot = Circle((x, y), radius=self.dot_radius, color='green', alpha=0.7)
        self.ax.add_patch(self.dot)

        self.create_sector()

        # Add the instance to the class-level list
        self.instances.append(self)

    def create_sector(self):
        self.sector = Wedge((self.dot.center[0], self.dot.center[1]), self.sector_radius, 0, self.sector_angle, color='red', alpha=0.3)
        self.ax.add_patch(self.sector)

    def update_sector(self):
        self.sector.set_radius(self.sector_radius)
        self.sector.set_theta1(0)
        self.sector.set_theta2(self.sector_angle)

    def rotate_sector(self, angle):
        current_theta1 = self.sector.theta1
        current_theta2 = self.sector.theta2
        self.sector.set_theta1(current_theta1 + angle)
        self.sector.set_theta2(current_theta2 + angle)

    def increase_sector(self):
        self.sector_angle += 1
        self.update_sector()

    def decrease_sector(self):
        if self.sector_angle > 1:
            self.sector_angle -= 1
            self.update_sector()

def on_click(event, rbs_list):
    if event.button == 1:  # Left-click
        x, y = event.xdata, event.ydata
        rbs = RBS(ax, x, y)
        RBS.selected_instance = rbs
        plt.draw()

def on_scroll(event, rbs_list):
    if RBS.selected_instance is not None:
        angle = event.step  # event.step is positive for forward scroll, negative for backward scroll
        RBS.selected_instance.rotate_sector(angle)
        plt.draw()

def on_key(event, rbs_list):
    if RBS.selected_instance is not None:
        if event.key == '+':
            RBS.selected_instance.increase_sector()
            plt.draw()
        elif event.key == '-':
            RBS.selected_instance.decrease_sector()
            plt.draw()

# Set the dimensions of the raster
width, height = 20, 20

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the raster
for y in range(height + 1):
    ax.plot([0, width], [y, y], color='black')

for x in range(width + 1):
    ax.plot([x, x], [0, height], color='black')

# Set axis limits
ax.set_xlim(0, width)
ax.set_ylim(0, height)

# Set aspect ratio to be equal, so the cells are square
ax.set_aspect('equal', adjustable='box')

# Remove axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])

# Connect the left-click event to the function
fig.canvas.mpl_connect('button_press_event', lambda event: on_click(event, RBS.instances))

# Connect the scroll event to the function
fig.canvas.mpl_connect('scroll_event', lambda event: on_scroll(event, RBS.instances))

# Connect the key events to the functions
fig.canvas.mpl_connect('key_press_event', lambda event: on_key(event, RBS.instances))

# Display the plot
plt.show()
