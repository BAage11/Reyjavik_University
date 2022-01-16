import time


def validateServiceData(service_data):  
    """ Returns a message to user, either if the data registered is valid (True) or if the data registererd is invalid (False). If invalid, then an error message is returned to user. """
    error_message = validateHourly(service_data['hourly_rate'])
    if(error_message != ''):
        return error_message

    error_message = validateTime(service_data['date_available'])
    if(error_message != ''):
        return error_message
    
    error_message = validateDateAvailable(service_data['date_available'])
    if(error_message != ''):
        return error_message

    return ''


def validateName(name):
    """ Check to see if user input for user name is valid:  1) Name inputed is at least 4 characters, 2) Name is a string. """
    return len(name) < 4 or name.replace(' ', '').isalpha() == False


def validateHourly(hourly):
    """ Check to see if user input for price per hour is valid:  1) Input is larger than zero, 2) Hourly rate is digits. """
    if(hourly == None or hourly == ''):
        return 'Invalid Hourly Rate: There must be some hourly rate fee.'

    parts = hourly.split('.')

    if(parts[0] == ''):
        parts[0] = '0'
    money = parts[0]
    
    if(len(parts) == 1):
        
        if(money == '0'):
                return 'Invalid Hourly Rate: There must be some hourly rate fee.'
        if((money.isdigit())==False):
            print(money)
            try:
                int(money)
            except Exception:
                return 'Invalid Hourly Rate: Hourly rate must only contain numbers, no alphabetical letters.qwerqwer'
        if((0 <= int(money))==False):
            return 'Invalid Hourly Rate: Hourly rate must be a positive number.'
    
    if(len(parts) == 2):
        if(parts[0] == ''):
            parts[0] = '0'
        if(parts[1] == ''):
            parts[1] = '0'

        money = parts[0]
        cents = parts[1]

        if(money == '0' and cents == '0'):
            return 'Invalid Hourly Rate: There must be some hourly rate fee.'
        elif((0 <= int(money))==False):
            return 'Invalid Hourly Rate: Hourly rate must be a positive number.'
        elif((0 <= int(cents) < 100) == False):
            return 'Invalid Hourly Rate: Hourly rate cant have more than .99 cents.'
        elif((money.isdigit() and cents.isdigit())==False):
            return 'Invalid Hourly Rate: Hourly rate must only contain numbers, no alphabetical letters.asdf'
    
    return ''


def validateDateAvailable(days_and_times):
    """ Check to see if the date registered for new service is valid or not. The time of services cannot collide with each other, and there can not be more than two services per day from the same user. """
    days = {}
    for day_and_time in days_and_times:
        if(day_and_time[0] in days):
            if(len(days[day_and_time[0]]) >= 2):
                return "Invalid Dates: Can't have more than 2 services per day."
            else:
                days[day_and_time[0]].append(day_and_time[1:])

                if(validateSameDayServiceTimes(days[day_and_time[0]][0], days[day_and_time[0]][1])):
                    return "Invalid time on same day: Service times intersects each other."
        else:
            days[day_and_time[0]] = [day_and_time[1:]]

    return ''


def validateTime(dates):
    """ Check to see if user input for time is: 1) On the format HH:MM, for example 18:35, 2) That value for 'Hour' is between 0 and 24, 3) That value for 'Minutes' is between 00 and 59. """
    for date in dates:
        try:
            from_hour, from_min = date[1].split(':')
            to_hour, to_min = date[2].split(':')
        except Exception:
            return 'Invalid Time: Time must have ":" to seperate hours and minutes.'
        try:
            from_hour = int(from_hour) 
            from_min = int(from_min)
            to_hour = int(to_hour)
            to_min = int(to_min)
        except Exception:
            return 'Invalid Time: Time must contain only numbers.'
        
        list_of_times= [[from_hour, from_min], [to_hour, to_min]]
        for times in list_of_times:
            error_message = validateTimes(times)

            if error_message != '':
                return error_message

        if(from_hour > to_hour or (from_hour == to_hour and from_min > to_min)):
            return 'Invalid Time: From time must be before the To time.'

        elif((from_hour == to_hour and ((to_min - from_min) < 30)) or (((60*(to_hour-from_hour)+to_min)-from_min) < 30)):
            return 'Invalid Time: Total time of the service must be 30 min or more.'   

    return ''


def validateTimes(times):
    """ Check to see if the time registered (hour:minutes) is within the valid time limits of 24 hours and 60 minutes. """ 
    hour = times[0]
    min_ = times[1]
    
    if((0 <= hour < 24) == False):
        return 'Invalid Time: Hour must be between 0-23.'
    
    if((0 <= min_ < 60) == False):
        return 'Invalid Time: Minutes must be between 0-59.'
    
    return ''


def validateSameDayServiceTimes(time1, time2):
    """ Validation that the new services registered to not collide. If they collide, the function returns 'False' and an error message is returned to user (within another function). """
    time1_from_hour, time1_from_min = time1[0].split(':')
    time1_to_hour, time1_to_min = time1[1].split(':')

    time1_from_hour = int(time1_from_hour)
    time1_from_min = int(time1_from_min)
    time1_to_hour = int(time1_to_hour)
    time1_to_min = int(time1_to_min)


    time2_from_hour, time2_from_min = time2[0].split(':')
    time2_to_hour, time2_to_min = time2[1].split(':')

    time2_from_hour = int(time2_from_hour)
    time2_from_min = int(time2_from_min)
    time2_to_hour = int(time2_to_hour)
    time2_to_min = int(time2_to_min)


    if((time1_to_hour < time2_from_hour or (time1_to_hour == time2_from_hour and time1_to_min <= time2_from_min) 
    or time2_to_hour < time1_from_hour or (time2_to_hour == time1_from_hour and time2_to_min <= time1_from_min)) == False):
        return True

    return False
