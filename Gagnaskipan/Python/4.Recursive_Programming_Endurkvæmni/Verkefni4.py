# Prenta út fyrstu n náttúrulegu tölur 
# ○ Útfærið fall sem prentar út fyrstu n náttúrulegu tölur með endurkvæmri forritun 
# ■ úttak í einni línu 
# ○ natural(n) 
# ○ Náttúrulegar tölur: heilar jákvæðar tölur > 0 
# ■ natural(5) ● output: ​1 2 3 4 5 

def natural(number):
 #   prt_str = ""
    if number > 0:
#        prt_str += str(number)
        natural(number-1)
        print(number, end=" ")
#    return prt_str

natural(5)
