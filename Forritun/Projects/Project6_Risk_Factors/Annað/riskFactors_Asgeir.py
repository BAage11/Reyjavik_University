#Import the initial data to the program
def get_data ():
    file = open('riskFactors.csv', "r")
    whole = ''
    for words in file:
        whole+=words
    whole = whole.split('\n')
    file.close()
    return whole

# Get the indicators we are working with
def factors(whole):
    indicators = whole[0]
    indicators = indicators.split(',')
    whole.pop(0)
    indicators = sorted(indicators)
    used_indicators = [indicators[1], indicators[3], indicators[9], indicators[11], indicators[15]]
    indicators = used_indicators
    return indicators
#Make a large list consisting of smaller lists consisting of state data
def listed_states (data):
    state_list = []
    for state_data in data:
        state_data = state_data.split(',')
        state_list.append(state_data)
    return state_list

data = get_data()
indicators = factors(data)
state_list = listed_states(data)


print (state_list)
print ('------------------')
print (                  )
print ('------------------')
print (indicators)
