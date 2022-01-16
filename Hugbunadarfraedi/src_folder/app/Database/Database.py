import csv
import os
import json


class Database:
    def __init__(self):
        self.__service_filename = "../DatabaseCSV/Service.csv"
        self.__user_filename = "../DatabaseCSV/User.csv"
        self.__order_filename = "../DatabaseCSV/Order.csv"
        
        self.__service_absolute_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.__service_filename)
        self.__user_absolute_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.__user_filename)
        self.__order_absolute_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.__order_filename)

        self.__next_service_id = 0
        self.__next_user_id = 0
        self.__next_order_id = 0


    def getServices(self):
        """ Returns all of the registered cleaning services in database. 
            Format: ServiceUserName, HourlyRate, DaysAvailable """

        with open(self.__service_absolute_path, "r+") as csvfile:
            reader = csv.reader(csvfile)
            return_value = {}

            for index, row in enumerate(reader):
                if index != 0:
                    row[-1] = row[-1][2:-2].split('], [')
                    weekday = []
        
                    for day in row[-1]:
                        weekday.append(day.replace("'", "").split(', '))
                        
                    return_value[row[0]] = "{}/{}/{}".format(row[0],row[1],weekday)

            # Convert dict to json
            json_return = json.dumps(return_value)
            return json_return


    def writeServices(self, services):
        with open(self.__service_absolute_path, 'w+') as csvfile:
            csvfile.write("{}".format('id,user_id,service_name,hourly_rate,days_available'))
            for service in services:
                service_data = service.split('/')
                csv_data = '"{}","{}","{}","{}","{}"'.format(service_data[0], service_data[1], service_data[2], service_data[3], service_data[4])
                csvfile.write("\n{}".format(csv_data))
        

    def getOrders(self):
        """ Implementing an auto-increment for the ID of service. """
        check = False
        if(self.__next_order_id == 0):
            check = True

        with open(self.__order_absolute_path, "r+") as csvfile:
            reader = csv.reader(csvfile)
            return_value = {}

            for index, row in enumerate(reader):
                if index != 0:
                    if(check):
                        curr_id = int(row[0])
                        if(curr_id > self.__next_order_id):
                            self.__next_order_id = curr_id
                    return_value[row[0]] = "{}/{}/{}/{}/{}/{}".format(row[0],row[1],row[2],row[3],row[4],row[5])

            if(check):
                self.__next_order_id += 1
            
        return return_value
    
    def writeOrder(self, data):
        """ Writes a new order into the order.csv file """
        # Formats the data correctly before inserting it into the csv file.
        csv_format = '{}"","{}","{}","{}","{}","{}"'.format(self.__next_order_id, data["servicer_name"], data["customer_name"], data["hourly_rate"], data["date_available"], data["month_day"])
        self.addNewData(csv_format, "order")
    
    def getUsers(self):
        """ Fetches all of the users from the database User.csv, and returns a dictionary containing all users in the system. """
        with open(self.__user_absolute_path, "r+") as csvfile:
            reader = csv.reader(csvfile)
            user_dictionary = {}

            # Go through each line and store it in a dictionary
            for index, row in enumerate(reader):
                # Skip the first line
                if index != 0:
                    user_dictionary[row[0]] = "{}".format(row[1])

            return user_dictionary


    def addNewData(self, csv_data, path):
        """ Creates a new record in the relevant database containing the newly registered service/user/etc. """
        with open(self.getAbsolutePath(path), "a+") as csvfile:
            csvfile.write("\n{}".format(csv_data))


    def getAbsolutePath(self, path):
        """ Increments the highest current ID by one, for new registration(s). """
        if path == "service":
            self.__next_service_id += 1
            return self.__service_absolute_path
        
        elif path == "user":
            return self.__user_absolute_path
        
        elif path == "order":
            self.__next_order_id += 1
            return self.__order_absolute_path
        
        raise SystemExit('404 Error: Path not found.')


    def getServiceNextId(self):
        """ Returns the next ID in database (highest ID + 1) from service.csv """
        return self.__next_service_id


    def getOrderNextId(self):
        """ Returns the next ID in database (highest ID + 1) from order.csv """
        return self.__next_order_id 

if __name__ == "__main__":
    d = Database()
    #dummy_data = {"customer_name": "Carlos", "servicer_name": "Carlos2", "hourly_rate": "9.50", "date_available": ["Monday", "9:00", "10:00"], "month_day": "7.10.19"}
    #d.writeOrder(dummy_data)
    #data = ["1/1/Hougo Alveres/9.50/[['Monday', '9:00', '10:00'], ['Monday', '11:00', '12:50']]", "2/2/Ager/9.50/[['Monday', '9:00', '10:00'], ['Monday', '11:00', '12:50']]"]
    #d.writeServices(data)
    print(d.getOrders())
