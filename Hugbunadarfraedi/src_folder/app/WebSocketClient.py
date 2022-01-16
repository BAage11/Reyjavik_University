import asyncio
import websockets
import json

from datetime import date
import datetime
from datetime import timedelta

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


class MainMenu():
    def __init__(self):
        # By default user is not logged in
        self.user = None

    async def sendRegisteredService(self, hourly_rate, date_available):
        """ Gets all the valid necessary data for a new service (from user), and sends it to the server. """
        # Connection made to the server
        async with websockets.connect("ws://localhost:8765") as websocket:
            # Gets valid name from user, or sends an error message to user for invalid input
            #name = getValidInput('Name: ', validateName, 'Invalid Name: Name must be 4 or more letters and contain only characters.')
            # Gets valid hourly rate from user, or sends an error message to user for invalid input
            #hourly_rate = getValidInput('Hourly Rate: ', validateHourly, 'Invalid Hourly Rate: Hourly Rate must be bigger than 0 and contain only numbers.')
            # Get valid date (weekday(s) and time(s)) from user, or sends an error message to user for invalid input
            #date_available = getValidDate('> ', validateDate, 'Input must be numbers between 1 and 7, separated by commas.')
            # Creates new JSON data to send to the server, from the input registered by user
            json_data = json.dumps({'op': 'addNewService',
                                    'user_name': self.user,
                                    'hourly_rate': hourly_rate,
                                    'date_available': date_available})
            # Sends the JSON data to the server                        
            await websocket.send(json_data)
            # Gets back from server whether JSON data sent was handled successfully (or not)
            return_value = await websocket.recv()
            
            #return_value = json.loads(return_value)
            # Returns message to user if the registration was succesful (or not succesful)
            return return_value

    async def deleteService(self):
        """ Function to delete a previously registered service from the system, requested by the user. """
        # Connection made to the server
        async with websockets.connect("ws://localhost:8765") as websocket:

            json_data = json.dumps({'op': 'deleteService'})
            # Sends the JSON data to the server                        
            await websocket.send(json_data)
            # Gets back from server whether JSON data sent was handled successfully (or not)
            return_value = await websocket.recv()

            # Returns message to user if the registration was succesful (or not succesful)
            return return_value

    async def sendRegisteredUser(self, username, password, validation):
        """ Sends information about new registered user to store in database within the system. """
        # Connection made to the server
        async with websockets.connect("ws://localhost:8765") as websocket:
            json_data = json.dumps({'op': 'addNewUser',
                                    'username': username,
                                    'password': password,
                                    'validation': validation})
            # Sends the JSON data to the server                        
            await websocket.send(json_data)
            # Gets back from server whether JSON data sent was handled successfully (or not)
            return_value = await websocket.recv()
            # Returns message to user if the registration was succesful (or not succesful)
            return return_value

    async def fetchFromServer(self, dataToFetch):
        """ Fetches all registered services (from the server) which are currently available. """
        # Connection made to the server
        async with websockets.connect("ws://localhost:8765") as websocket:
            # Sets the operation in JSON format to fetchAllData ('dataToFetch' from input when function is invoked)
            json_data = json.dumps({'op': dataToFetch})
            # Sends the JSON operation to the server
            await websocket.send(json_data)
            # Receives all the currently registered services from the server
            services = await websocket.recv()
            # Returns the services available
            return services


    # Menu for user to register a new cleaning service
    def serviceRegistration(self, hourly, date):
        """ Visible part of the user, when selected to register new cleaning service. """
        # sendRegisteredService() function envoked for registration of new cleaning service
        msg = asyncio.get_event_loop().run_until_complete(self.sendRegisteredService(hourly, date))
        # Message printed out if registration was successful, or an error message if registration was not succesful
        msg = json.loads(msg)
        return msg
    
    # Menu for user to register a new cleaning service
    def userServiceDelete(self):
        """ Visible part of the user, when selected to register new cleaning service. """
        #print(" ------- Service Registration -------- ")
        # sendRegisteredService() function envoked for registration of new cleaning service
        msg = asyncio.get_event_loop().run_until_complete(self.deleteService())
        # Message printed out if registration was successful, or an error message if registration was not succesful
        msg = json.loads(msg)
        return msg

    def userRegistration(self, username, password, validation):
        """ Visible part of the new user registration """
        # sendRegisteredUser() function envoked for registration of new user
        msg = asyncio.get_event_loop().run_until_complete(self.sendRegisteredUser(username, password, validation))
        # Message printed out if registration was successful, or an error message if registration was not succesful
        return msg
    
    def logOut(self):
        """ A function so the user whom is logged in, can log out of his/her account. """
        self.user = None
        return "User has been logged out"

    def loginUser(self, username, password):
        """ Function for user to log in to the system, so he/she can access the functionality within the system. """
        # sendLoginDetails() function envoked for login of user
        msg = asyncio.get_event_loop().run_until_complete(self.sendLoginDetails(username, password))
        # User is logged in and username is stored in init function
        self.user = msg
        # Message printed out from the function
        return msg

    async def sendLoginDetails(self, username, password):
        """ Connection made between client and server, so user can access the system. """
        # Connection made to the server
        async with websockets.connect("ws://localhost:8765") as websocket:
            # User input sent via json
            json_data = json.dumps({'op': 'logInUser', 
                                'username': username,
                                'password': password
                                })
            await websocket.send(json_data)
            # Return value received from the server
            return_value = await websocket.recv()
            return return_value


    def getServices(self):
        """ Function where all available registered cleaning services are listed out on the screen. """ 
        # Use of fetchFromServer() function to get all current registered services, using websockets
        services = asyncio.get_event_loop().run_until_complete(self.fetchFromServer("getServices"))
        services = json.loads(services)
        #print("Services:",services)

        orderes = asyncio.get_event_loop().run_until_complete(self.fetchFromServer("getOrderes"))
        orderes = json.loads(orderes)
        #print("Orders:",orderes)

        # All services listed out, with given key for service in database
        for key, service in services.items():
            service_user_name, hourly_rate, days_available  = service.split('/')
            days_available = days_available[2:-2].split('], [')
            days = []
            for day in days_available:
                days.append(day.replace("'", "").split(', '))

            month_days = self.getMonthDays(key, days, orderes)
            services[key] += "/{}".format(month_days)

        # Formats the services retrieve from fetchFromServer() to a dictionary form (JSON)
        return services
    
    
    def getMonthDays(self, service_name, days, orderes):
        """ This is a REALY tricky function and if time would allow us we would probably clean it up but... it works
            This function returns the month days the service is available.
            f.x. If someone has already ordered 'Hougo Alvares' on the monday 7.10.19 we would return the NEXT 4 mondays (14, 21,28 and 4) """
        curr_date = date.today()
        month_days = []

        days_times_and_names_occupied = []
        # Get all the orderes into a confortable format for later checks, Format = [['service_name', ['weekday','time','time'],...], 'date']
        for key, order in orderes.items():
            #print(order)
            Order_id, ServiceUserName ,UserName ,HourlyRate ,DayAvailable ,Date = order.split('/')
            
            if(ServiceUserName != service_name):
                break
            year, month, day_holder = Date.split('-')
            if(len(month) == 1):
                month = "0"+month
            if(len(day_holder) == 1):
                day_holder = "0"+day_holder 
            
            value_str = "{}-{}-{}".format(year, month, day_holder)
            day_and_time_occupied = DayAvailable[1:-1].replace("'", "").split(', ')
            days_times_and_names_occupied.append([ServiceUserName, day_and_time_occupied, value_str])

        # Goes through the days in services and checks if there are any orderes on that day
        # If there are any orderes on that day we dont get that exact day, 
        # f.x. If someone has already ordered 'Hougo Alvares' on the monday 7.10.19 we would return the NEXT 4 mondays (14, 21,28 and 4)
        for day in days:
            curr_month_days = []

            # Get the current monthly day for that weekday
            nr_day_in_week = self.getDayNumber(day[0])
            day_shift = (nr_day_in_week - curr_date.weekday()) % 7
            curr_month_day = curr_date + datetime.timedelta(days=day_shift)

            # While we dont have 4 monthly days we continue searching for them
            while(len(curr_month_days) < 4):
                add = True
                # Go through all the occupied times and if the day is not occupied we add him to curr_month_days
                for day_time_and_name_occupied in days_times_and_names_occupied:
                    # Check if the day is already occupied
                    if(day_time_and_name_occupied[0] == service_name and day_time_and_name_occupied[1] == day and str(curr_month_day) == day_time_and_name_occupied[2]):
                        add = False
                        break
                # If the day was not occupied we add it to the curr_month_days
                if(add):
                    curr_month_days.append(str(curr_month_day))
                curr_month_day = curr_month_day + timedelta(days=7)
            # Here we have curr_month_days that is of the length 4 and contains 4 dates that are non occupied
            month_days.append(curr_month_days)
            
        return month_days

    
    def getDayNumber(self, date):
        """ Converts weekdays into ints, for example 'Monday' = 0, so when the function gets date = 'Monday' it returns 0. """    
        if('Monday' == date):
            return 0
        if('Tuesday' == date):
            return 1
        if('Wednesday' == date):
            return 2
        if('Thursday' == date):
            return 3
        if('Friday' == date):
            return 4
        if('Saturday' == date):
            return 5
        if('Sunday' == date):
            return 6

    async def bookService(self, service_user_name, hourly_rate, day_available, date):
        """ Connection made to server, so user can book a cleaning service within the system. """
        # Connection made to the server, using websockets
        async with websockets.connect("ws://localhost:8765") as websocket:
            json_data = json.dumps({'op': 'addBookedService',
                                'service_user_name': service_user_name,
                                'user_name': self.user,
                                'hourly_rate': hourly_rate,
                                'weekday': day_available,
                                'date': date})
        
            # Sends the JSON data to the server                        
            await websocket.send(json_data)
            # Gets back from server whether JSON data sent was handled successfully (or not)
            return_value = await websocket.recv()
            # Returns message to user if the registration was succesful (or not succesful)
            return return_value

    def orderService(self, service_user_name, hourly_rate, day_available, date):
        """ Function so the user can order available cleaning service within the system. """
        # Sends the nessasary info to the websocket
        results = asyncio.get_event_loop().run_until_complete(self.bookService(service_user_name, hourly_rate, day_available, date))
        # Returns the success message
        return results



if __name__ == '__main__':
    main = MainMenu()
    #main.mainMenu()
    #a = main.loginUser("John", "Hundur")
    #print(a)

    print("\n",main.userRegistration('JohnI','Addidaddi','Addidaddi'))
