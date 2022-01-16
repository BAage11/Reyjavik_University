# Implement a class called Clock with the following attributes:
# Constructor with three parameters: hours, minutes, seconds with default values 0.
# Three instance variables: hours, minutes, seconds.
# A method called str_update(). It takes as an argument a string of the form hh:mm:ss and updates the three instances variables.
# A __str__() method for responding to the print() method. It should write out: "{} hours, {} minutes and {} seconds"
# A method called add_clocks(). It takes another clock object as a parameter, adds the two clocks and returns a new clock instance.  In this method, you need to add the respective values of the two clocks together and remember the resulting hours, minutes and seconds. Remember that the sum of seconds cannot exceed 60, in which case there is a carry over to the minutes values. Same for minutes, it cannot exceed 60 and carries over to hours. For hours, the summed values cannot exceed
# 23. If hours is exceeded, we ignore it.  Use the divmod() built-in Python function in your implementation.

class Clock():
  def __init__(self, hours=0, minutes=0, seconds=0):
    self.hours = hours
    self.minutes = minutes
    self.seconds = seconds

  def str_update(self, time=""):
    update_time = time.split(":")
    self.hours = int(update_time[0])
    self.minutes = int(update_time[1])
    self.seconds = int(update_time[2])

  def __str__(self):
    return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)

  def add_clocks(self, param1):
    new_clock = Clock()
    total_sec = self.seconds + param1.seconds
    add_min, rem_sec = divmod(total_sec, 60)
    total_min = self.minutes + param1.minutes + add_min
    add_hrs, rem_min = divmod(total_min, 60)
    total_hrs = self.hours + param1.hours + add_hrs
    extra, total_hrs = divmod(total_hrs, 24)
        
    new_clock.str_update("{}:{}:{}".format(total_hrs, rem_min, rem_sec))
    return new_clock

clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)
# assert str(clock1) == "20 hours, 10 minutes and 52 seconds"

print(clock2)
# assert str(clock2) == "8 hours, 49 minutes and 24 seconds"

clock3 = clock1.add_clocks(clock2)
print(clock3)
# assert str(clock3) == "5 hours, 0 minutes and 16 seconds"