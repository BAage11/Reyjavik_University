# Blaðsíða 405 - Code listing 7.18

import pylab

# Generate lists of points for both sine and cosine
x_values = pylab.linspace(0, 4*pylab.pi, 100)
y1_values = pylab.sin(x_values)
y2_values = pylab.cos(x_values)

# Plot two curves on the same graph
pylab.title("Sine and Cosine Plot")
pylab.plot(x_values, y1_values, "b")
pylab.plot(x_values, y2_values, "r")
pylab.show()
