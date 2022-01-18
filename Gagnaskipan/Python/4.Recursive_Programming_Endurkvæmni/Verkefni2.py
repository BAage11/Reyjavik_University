# Margföldun með einungis +/- 
# ○ Útfærið margföldun tveggja jákvæðra heiltalna með endurkvæmri forritun 
# ○ multiply(a, b) 
# ○ Byrjið á jákvæðum heiltölum 
# ■ Veltið einnig fyrir ykkur hvernig lausnin gæti virkað með neikvæðum heiltölum líka 

def multiply(a,b):
    if b <= 0:
        return 0
    else: 
        return a + multiply(a,b-1)


print(multiply(2,2))