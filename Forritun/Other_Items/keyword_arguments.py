def cm(feet = 0, inches = 0):
  inches_to_cm = inches * 2.54
  feet_to_cm = feet * 12 * 2.54
  return inches_to_cm + feet_to_cm

centim = cm(feet = 5)
print(centim)

