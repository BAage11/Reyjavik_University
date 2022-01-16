import unittest
import json

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../app"))

from WebSocketClient import MainMenu

class AddServiceTests(unittest.TestCase):

    ############################################# HOURLY RATE TESTS #############################################

    def test_AddIncorrectNoHourlyRateServiceTest(self):
        
        # 1 No Hourly fee
        hourly_no_fee_test = ["","0", "0.0", None]
        for hourly_fee in hourly_no_fee_test:
            results = self.setUp().serviceRegistration(hourly_fee, [])
            self.standardResultsTest(results, False)
            #print(hourly_fee, results['error_message'], 'Invalid Hourly Rate: There must be some hourly rate fee.')
            self.typeAndValueTest(results['error_message'], '', 'Invalid Hourly Rate: There must be some hourly rate fee.')
    
    def test_AddInncorrectOneNumberHourlyRateServiceTest(self):
        # 2 One number Hourly fee
        hourly_one_number_test = ['-1', 'abcd']
        error_message = ['Invalid Hourly Rate: Hourly rate must be a positive number.','Invalid Hourly Rate: Hourly rate must only contain numbers, no alphabetical letters.']
        for i in range(len(hourly_one_number_test)):
            results = self.setUp().serviceRegistration(hourly_one_number_test[i], [])
            self.standardResultsTest(results, False)
            #print(hourly_one_number_test[i], results['error_message'], error_message[i])
            self.typeAndValueTest(results['error_message'], '', error_message[i])
    


    def test_AddIncorrectTwoNumberHourlyRateServiceTest(self):
        hourly_two_number_test = ['-1.10', 'abcd.abc', '10.abc', '10.100']
        error_message = ['Invalid Hourly Rate: Hourly rate must be a positive number.',
                        'Invalid Hourly Rate: Hourly rate must only contain numbers, no alphabetical letters.',
                        'Invalid Hourly Rate: Hourly rate must only contain numbers, no alphabetical letters.',
                        'Invalid Hourly Rate: Hourly rate cant have more than .99 cents.']
        for i in range(len(hourly_two_number_test)):
            results = self.setUp().serviceRegistration(hourly_two_number_test[i], [])
            self.standardResultsTest(results, False)
            #print(hourly_two_number_test[i], results['error_message'], error_message[i])
            self.typeAndValueTest(results['error_message'], '', error_message[i])


    ############################################# DATE TESTS #############################################

    def test_AddIncorrectDateAvailableServiceTest(self):
        date_available_test = [['Monday', '9:00', '10:00'], ['Monday', '11:00', '12:00'], ['Monday', '13:00', '14:00']]

        results = self.setUp().serviceRegistration('1.10', date_available_test)
        self.standardResultsTest(results, False)
        #print(date_available_test, results['error_message'], "Invalid Dates: Can't have more than 2 services per day.")
        self.typeAndValueTest(results['error_message'], '', "Invalid Dates: Can't have more than 2 services per day.")

    def test_AddIncorrectDateTimesServiceTest(self): 
        date_available_test = [
            [['', '25:00', '8:00']],
            [['', '-1:60', '8:00']],
            [['', '2:60', '8:00']],
            [['', '20:-1', '8:00']],
            [['', '9:00', '8:00']],
            [['', '9:00', '9:29']],
            [['', '9:35', '10:04']]]

        error_message = ['Invalid Time: Hour must be between 0-23.',
                        'Invalid Time: Hour must be between 0-23.',
                        'Invalid Time: Minutes must be between 0-59.', 
                        'Invalid Time: Minutes must be between 0-59.',  
                        'Invalid Time: From time must be before the To time.', 
                        'Invalid Time: Total time of the service must be 30 min or more.', 
                        'Invalid Time: Total time of the service must be 30 min or more.'] 

        for i in range(len(date_available_test)):
            results = self.setUp().serviceRegistration('1.10', date_available_test[i])
            self.standardResultsTest(results, False)
            #print(date_available_test[i], results['error_message'], error_message[i])
            self.typeAndValueTest(results['error_message'], '', error_message[i])
    
    def test_AddIncorrectSameDateTimeServiceTest(self): 
        date_available_test = [
            [['Monday', '9:00', '10:00'], ['Monday', '9:30', '11:00']],
            [['Monday', '9:30', '11:00'], ['Monday', '9:00', '10:00']]]


        for i in range(len(date_available_test)):
            results = self.setUp().serviceRegistration('1.10', date_available_test[i])
            self.standardResultsTest(results, False)
            #print(date_available_test[i], results['error_message'], "Invalid time on same day: Service times intersects each other.")
            self.typeAndValueTest(results['error_message'], '', "Invalid time on same day: Service times intersects each other.")


    ############################################# ADD CORRECT INFO SERVICE #############################################

    #def test_AddCorrectServiceTest(self):
    #    
    #    # Set Up
    #    self.setUp().userServiceDelete()
#
    #    name = "Hougo Alveres"
    #    date = [['Monday','9:00','10:00'], ['Monday','11:00','12:00']]
    #    hourly_rate = '9.50'
    #    results = self.setUp().serviceRegistration(hourly_rate, date)
    #    if 'error_message' in results:                                                    
    #        print(results['error_message'], "<= This vas the error")
#
    #    self.standardResultsTest(results, True)
#
    #    self.assertTrue(type(results['success_message']) == type(''))
    #    self.assertTrue(results['success_message'] != '')
    #    self.assertEqual(results['success_message'], "Added new Service: Name: Hougo Alveres, Hourly: 9.50, Date: [['Monday', '9:00', '10:00'], ['Monday', '11:00', '12:00']]")
#
    #    self.setUp().userServiceDelete()

    ############### HELPING FUNCTIONS ###############

    def setUp(self):
        return MainMenu()
    
    def standardResultsTest(self, results, correct):

        self.assertTrue(type(results) == type({}))
        
        if(correct):
            self.assertTrue('success_message' in results)
            self.assertTrue('error_message' not in results)
        else:
            self.assertTrue('success_message' not in results)
            self.assertTrue('error_message' in results)
    
    def typeAndValueTest(self, object_to_test, type_to_test_for, value):
        self.assertTrue(type(object_to_test) == type(type_to_test_for))
        self.assertTrue(object_to_test == value)

if __name__ == "__main__":

    unittest.main()