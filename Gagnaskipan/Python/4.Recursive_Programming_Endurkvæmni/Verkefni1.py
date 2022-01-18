# Veldi 
# ○ Útfærið aðgerð sem hefur tölu upp í jákvætt heiltöluveldi með endurkvæmri forritun 
# ○ power(base, exp) 

def power(base, exp):
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)


result = power(2, 8)
print(result)
