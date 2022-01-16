# Einstein's famous equation states that the energy in an object at rest equals its mass times the square of the speed of light.  (The speed of light is 300,000,000 m/s.)
 
# Complete the skeleton code below so that it:
# * Accepts the mass of an object (remember to convert the input string to a number, in this case, a float).
# * Calculate the energy, e
# * Prints e

m_str = input('Input m: ')  # do not change this line
m_float = float(m_str)
# change m_str to a float

# remember you need c 
c = 300000000

# e = 
e = m_float * (c**2)
print("e =", e)  # do not change this line
