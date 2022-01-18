# Þversumma jákvæðra heilla talna 
# ○ Útfærið fall sem reiknar og skilar þversummu færibreytu með endurkvæmri forritun 
# ○ # sum_of_digits(x) 
# ○ Summa allra tölustafa tölunnar í tugakerfinu 
# ■ þversumma 254 = 2+5+4 = 11 
# ■ print(sum_of_digits(254)) 
# ● output: ​11

def sum_of_digits(number):
    if number < 10:
        return number
    return (number % 10 + (sum_of_digits(number // 10)))



print(sum_of_digits(1024))

print()
print(254 % 10)
print(25 % 10)
print(2 % 10)

print()
print(254 // 10)
print(25 // 10)
print(2 // 10)
