top_num = int(input("Please type a number between 0 and 999: "))

for i in range(top_num):
  total = 0
  n = len(str(i))

  for j in range(1, i):
    total += int(j)**n
  if total == i:
    print (i)

# Athuga villuna, á að vera 0-9, 153, 370, 371 og 407 (þegar top_num = 596)
