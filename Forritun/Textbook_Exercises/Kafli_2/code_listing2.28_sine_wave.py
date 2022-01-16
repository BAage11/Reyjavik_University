# Blaðsíða 178 - Code listing 2.28
# Plot a sine wave from 0 to 4pi

import math
import pylab

# Initialize the two lists and the counting variable num. Note is a float
y_values = []
x_values = []
number = 0.0

# Collect both number and the sine of number in a list
while number < math.pi * 4:
  y_values.append(math.sin(number))
  x_values.append(number)
  number += 0.1

# Plot the x and y values as red circles
pylab.plot(x_values, y_values, "ro")
pylab.show()
