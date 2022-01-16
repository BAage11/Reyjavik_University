# Positions of relevant data in risk factor file
STATE = 0
HEART_DISEASE = 1
MOTOR_VEHICLE = 5
TEEN = 7
SMOKING = 11
OBESITY = 13

def read_risk_factors(name):
    ''' Reads the given risk factors file and returns a list of all the lines.
        The first element in the returned list is a list of headers
    '''
    try:
        risk_factors_list = []
        fp = open(name,'r')
        for line in fp:
            line = line.strip()
            line = line.split(',')
            risk_factors_list.append(line)
    except FileNotFoundError:
        print("Cannot find file", name)
    return risk_factors_list
    
def find_min_max(a_list):
    """ Required
        -- list with a header value plus 51 string values
        Return
        -- min_value, max_value """
    if '%' in a_list[1]:
        values = [float(num[:-1]) for num in a_list[1:]]
    else:
        values = [float(num) for num in a_list[1:]]

    min_val = min(values)
    max_val = max(values)
    min_index = values.index(min_val)
    max_index = values.index(max_val)
    
    return min_index, max_index, min_val, max_val

def build_output_string(indicator_list, states, min_index, max_index, min_val, max_val):
    min_state = states[min_index+1]
    max_state = states[max_index+1]
    return "{:33}{:21s}{:6.1f}{:6s}{:15s}{:6.1f}".format(indicator_list[0]+":",min_state,min_val,"",max_state,max_val)

def get_indicators(risk_factor_list):
    ''' Extracts and returns the individual indicators from the given list '''
    states = [lst[STATE] for lst in risk_factor_list]
    heart = [lst[HEART_DISEASE] for lst in risk_factor_list]
    motor = [lst[MOTOR_VEHICLE] for lst in risk_factor_list]
    teen = [lst[TEEN] for lst in risk_factor_list]
    smoking = [lst[SMOKING] for lst in risk_factor_list]
    obesity = [lst[OBESITY] for lst in risk_factor_list]
    return states, heart, motor, teen, smoking, obesity

def print_header():
    header_str = "{:33}{:21s}{:6s}{:6s}{:15s}{:6s}".format("Indicator","Min","","","Max","")
    line_str = '-'*87
    print(header_str)
    print(line_str)

def print_indicators(risk_factor_list):
    states, heart, motor, teen, smoking, obesity = get_indicators(risk_factor_list)

    for indicator in [heart, motor, teen, smoking, obesity]:
        min_index, max_index, min_val, max_val = find_min_max(indicator)
        output_str = build_output_string(indicator, states, min_index, max_index, min_val, max_val)
        print(output_str)    

# Main program starts here
filename = input("Enter filename containing csv data: ")
#risk_factor_list = read_risk_factors("/Users/hrafn/Namskeid/Forritun/Programs/homeworks/hw5/riskfactors.csv")
risk_factor_list = read_risk_factors(filename)

print_header()
if risk_factor_list:
    print_indicators(risk_factor_list)
    