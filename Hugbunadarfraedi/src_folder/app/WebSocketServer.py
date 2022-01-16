import asyncio
import json
import websockets

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from Database.Database import Database
from GetValidInfo.ValidateServiceData import validateServiceData
from GetValidInfo.ValidateNewUserReg import *


class ComponentInterface:
    """ Methods that the server can do, using access to the databases within the system. """
    # Connection to the database
    def __init__ (self):
        self.db = Database()
        self.getServices()
        self.getOrders()
    # Add new data into the system (database)
    def addNewData(self, data, path):
        self.db.addNewData(data, path)
    # Fetch all the Services
    def getServices(self):
        return self.db.getServices()
    # Re-write the services made within the database, when a service is deleted
    def writeServices(self, services):
        self.db.writeServices(services)
    # Get all registered orders made within the system
    def getOrders(self):
        return self.db.getOrders()
    # Get next ID for newly registered service
    def getServiceNextId(self):
        return self.db.getServiceNextId()
    # Get next ID for newly made order of service
    def getOrderNextId(self):
        return self.db.getOrderNextId()
    # Get all registered user within the system (database)
    def getUsers(self):
        return self.db.getUsers()


class ComponentPort:
    __instance = None

    # This is a class method - it can be called without an instance
    @staticmethod 
    def get_instance():
        """ Static access method. """
        # Tthe method makes sure that an instance is created, if none exists
        if ComponentPort.__instance == None:
            ComponentPort()      
        # The instance is returned
        return ComponentPort.__instance


    def __init__(self):
        """ The constructor throws an error if there is already an existing instance. """
        # If there is already an existing instance, throw an error
        if ComponentPort.__instance != None:
            raise Exception("This class is a singleton!")
        # ... else, create an instance
        else:
            ComponentPort.__instance = self
            self.iface = ComponentInterface()

    async def __request_handler(self, websocket, path):
        """ Handles all the client request using websockets. """
        # Wait to get the JSON format from the client
        msg = await websocket.recv()
        # ... then create a JSON object from the format received from the websocket client
        data = json.loads(msg)
        return_value = ''
        if("op" in data):
            # If value is 'addNewService', then call the functionality to add new service to the given database within the system
            if(data['op'] == 'addNewService'):
                return_value = {}

                # Check to see if service has already been registered within the system
                services = self.iface.getServices()
                services = json.loads(services)
                for key, service in services.items():
                    service_info = service.split('/')
                    if(service_info[1] == data['user_name']):
                        return_value['error_message'] = 'You already have registered service.'
                        break
                
                # If service is not yet registered in the system, check if registration is on a valid form and add it to the given database within the system. Else, send an error message to user what went wrong with the registration of service.
                if('error_message' not in return_value):
                    error_message = validateServiceData(data)
                    if(error_message == ''):
                        csv_data = '{}","{}","{}"'.format(data['name'], data['hourly_rate'], data['date_available'])
                        self.iface.addNewData(csv_data, "service")
                        # Returns succesfull text
                        return_value['success_message'] = 'Added new Service: Name: {}, Hourly: {}, Date: {}'.format(self.user['name'], data['hourly_rate'], data['date_available'])
                    else:
                        return_value['error_message'] = error_message
                # Return the message to the user, if service was successfully added to the system or with an error message what went wrong with the registration.
                return_value = json.dumps(return_value)
            
            if(data['op'] == 'getServices'):
                # Gets all registered serivces within the system, to be listed up by request from the user.
                string = self.iface.getServices()
                return_value = string
            
            if(data['op'] == 'addBookedService'):
                # Retrieves the selected service within the database, and removes it from the database service.csv (puts it as a booked service in order.csv instead) so it can not be booked twice.
                order_id = self.iface.getOrderNextId()
                csv_data = '"{}","{}","{}","{}","{}","{}"'.format(order_id, data["service_user_name"], data['user_name'], data["hourly_rate"], data["weekday"], data["date"])
                self.iface.addNewData(csv_data, "order")
                format_string = "Successfully booked service: {}, {} {}-{}. Hourly rate: {} on {}"
                return_value = format_string.format(data["service_user_name"], data["weekday"][0], data["weekday"][1], data["weekday"][2], data["hourly_rate"], data["date"])
            
            
            
            if(data['op'] == 'getOrderes'):
                # Retrieves all registered orders made within the system.
                return_value = json.dumps(self.iface.getOrders())

            if(data['op'] == 'addNewUser'):
                # Register a new user request within the database in the system.
                new_user_data = '"{}","{}","{}"'.format(data['username'], data['password'], data['validation'])


                if validateNewPassword(data['password'], data['validation']) == False:
                    return_value = 'Invalid Password: Password must be between 5 and 30 characters and must match Validation Password.'
                if return_value == '':
                    return_value = checkIfValidUsername(data['username'])
                    if return_value == '':
                        return_value = checkIfUserExists(data['username'])

                if return_value == '':
                    self.iface.addNewData(new_user_data, "user")
                    format_string = "New user registration succesful.\nNew username: {}\nNew password: {}"
                    return_value = format_string.format(data['username'], '*' * len(data['password']))      

            if(data['op'] == 'logInUser'):
                # Logs the user into the system, so he/she can use the functionalities within the system.
                #login_data = '{}/{}'.format(data["username"], data["password"])
                users_dict = self.iface.getUsers()
                #for key in users_dict:
                #    if users_dict[key] == login_data:
                #        username = users_dict[key].split("/")
                #        return_value = username[0]
                #        break
                if(data['username'] in users_dict):
                    print(users_dict[data['username']])
                    password = users_dict[data['username']].split('/')
                    if(password[0] == data['password']):
                        return_value = data['username']

                if return_value != data['username']:
                    return_value = 'Username/Password not Found.'
        else:
            # If instance contains an invalid format, an error message is created
            return_value = json.dumps({"msg":"Invalid data format"})
        # Sends correct output to the client (or error message, if invalid)
        await websocket.send(return_value)


    def start(self):
        """ Start the websocket server. """
        start_server = websockets.serve(self.__request_handler, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        print("Server started...")
        asyncio.get_event_loop().run_forever()
        print("Server stopped...")


if __name__ == '__main__':
    compPort = ComponentPort.get_instance()
    compPort.start()
