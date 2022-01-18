from random import Random

class Item():
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
    
    def __hash__(self):         
    # hash(item) kallið fyrir neðan, breytir item og nær í self fyrir klasann (alveg eins og __str__ fallið með print(item) sem verður þá print(self) í því falli).
        sum = 0
        for c in self.key:
            sum += ord(c)           
            # Gets the index in the ascii table for this particular letter
        return sum

def random_letter():
    val = rand.randint(0, 128)
    return chr(val)         # Changes the integer to an ascii letter



size = 100
rand = Random()
lis = [0] * size

for _ in range(1000):
    ch1 = random_letter()
    ch2 = random_letter()
    ch3 = random_letter()
    
    a_str = ch1 + ch2 + ch3
    
    item = Item(a_str, 0)
    index = hash(item) % size           
    # Sendir inn tilvik af klasanum inn í fallið __hash__, sem kallar þá á self í klasanum og vinnur með það.
    lis[index] += 1




print(lis)

