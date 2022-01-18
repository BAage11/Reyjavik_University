#TimeComplexity O(n)
import random

def getRandomNumber(min_, max_):
        #TimeComplexity O(1)
        return random.randint(min_, max_)

def randomList(list_to_random):
        #TimeComplexity O(n)
        for i in range(len(list_to_random)):
                list_to_random[i] = getRandomNumber(1,6)
        return list_to_random

print(randomList([0]*100))