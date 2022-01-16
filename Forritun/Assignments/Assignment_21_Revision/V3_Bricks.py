# We want to make a row of bricks that is goal_length inches long. We have a number of small_bricks bricks (1 inch each) and big_bricks bricks (5 inches each). Create a function that takes 3 parameter, the numbers of small_bricks bricks, the number of big_bricks bricks and the goal_length length. The function should return True if it is possible to make the goal_length long row by choosing from the given bricks. This can be done without any loops so don´t use any loops.

def check_bricks(small_bricks, big_bricks, goal_length):
  total = small_bricks + (big_bricks*5)

  if goal_length > total:
    # Ekki hægt að byggja goal_length, ekki nóg bricks
    return False
  
  if big_bricks != 0 and small_bricks != 0:
    # Tekur mið af því hvað liggur eftir, eftir að búið er að nota max big_bricks (5 inch each). Ef hægt er að klára remainder með small_bricks (það er small_bricks er stærri en goal_length), þá er hægt að klára goal_lenght = True
    remainder = goal_length % 5           
    if remainder - small_bricks <= 0:     
      return True
    else:
      return False
  
  elif big_bricks == 0 and small_bricks == 0:
    # Ef fjöldi small_bricks og big_bricks er 0, er ekki hægt að byggja goal_length.
    # Þar af leiðandi er þetta einungis True ef goal_length er líka 0, annars False.
    if goal_length == 0:
      return True
    else:
      return False

