# Write a class Student() such that it has an attribute 'score' (that is initialized with 10) and three methods:
# add_score(): adds 10 to the score
# decrease_score(): decreases score by 10
# __str__(): returns the current score (should return a string)

class Student():
  def __init__(self, score=10):
    self.score = score

  def __str__(self):
    return str(self.score)

  def add_score(self):
    self.score += 10
  
  def decrease_score(self):
    self.score -= 10


p = Student()
print(p)
p.add_score()
print(p)
p.decrease_score()
print(p)
