# Given seconds (int) calculate hours, minutes, and seconds.
# For example, given 80000 seconds that is
# 22 hours, 13 minutes, and 20 seconds.
# Hint 1: use integer division (//) and remainder (%)
# Hint 2: we require that you create and output variables hours, minutes, and seconds, but # you will likely find an additional variable useful.

secs_str = input("Input seconds: ") # do not change this line
secs_int = int(secs_str)

# hours (klst = 60 min * 60 sek)=
hours = secs_int // (60 * 60)

# minutes (tek afganginn af klst og reikna svo min.) =
minutes =  (secs_int % (60*60)) // 60 

# seconds (tek afganginn af mín.) =
seconds = secs_int % 60

print(hours,":",minutes,":",seconds) # do not change this line
