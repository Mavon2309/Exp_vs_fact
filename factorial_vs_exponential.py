import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import factorial
from scipy.special import factorial as sp_factorial

# Define the range for the x-axis
x = np.arange(0, 30, 0.1)
exp_growth = np.exp(x)

# Function to compute factorial values for non-integer x
def factorial_approx(x):
    return sp_factorial(x, exact=False)

# Create a figure and axis
fig, ax = plt.subplots()
line1, = ax.plot([], [], lw=2, label='Exponential (e^x)')
line2, = ax.plot([], [], lw=2, label='Factorial (n!)')
ax.legend()

# Setting the axes properties
ax.set_xlim(0, 30)
ax.set_ylim(0, np.exp(30))  # Adjust the y-axis limit to match the range of exponentials

# Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Animation function
def animate(i):
    x_i = x[:i]
    exp_y = exp_growth[:i]
    fact_y = factorial_approx(x[:i])
    
    line1.set_data(x_i, exp_y)
    line2.set_data(x_i, fact_y)
    return line1, line2

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x), interval=10, blit=True)

# Display the animation
plt.xlabel('x')
plt.ylabel('Growth')
plt.title('Comparison of Exponential and Factorial Growth')
plt.show()
