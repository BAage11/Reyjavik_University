# Blaðsíða 176 - Code listing 2.27

import pylab
list_of_ints = []

for counter in range(10):
  list_of_ints.append(counter * 2)

print(list_of_ints)
print(len(list_of_ints))

# Now plot the list
pylab.plot(list_of_ints)
pylab.show()
