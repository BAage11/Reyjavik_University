import unittest
import json

import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../app"))

from WebSocketClient import MainMenu

#from WebSocketClient import sendRegisteredService
from GetValidInfo import ValidateUserInput




class MainTestData(unittest.TestCase):
	def data_collection(self):
		main_menu = MainMenu()
		self.my_data = main_menu.sendRegisteredService()
		ValidationUserInfo()
		CreateNewRegisteredService()

class ValidationUserInfo(unittest.TestCase):
	def validNameTest(self):
		invalid_name = ValidateUserInput.validateName("jakob123")
		valid_name = ValidateUserInput.validateName("jakob")

		self.assertEqual(invalid_name == True)
		self.assertEqual(valid_name == False)
	
	def validateDateTest(self):

		invalid_date1 = ValidateUserInput.validateDate(["a"])
		invalid_date2 = ValidateUserInput.validateDate(["100"])
		invalid_date3 = ValidateUserInput.validateDate(["-100"])
		
		valid_date = ValidateUserInput.validateDate(["-100"])

		self.assertEqual(invalid_date1 == True)
		self.assertEqual(invalid_date2 == True)
		self.assertEqual(invalid_date3 == True)
		self.assertEqual(valid_name == False)



class CreateNewRegisteredService(unittest.TestCase):
	def test_collect(self):
		""" As we do not know anything about the values from the data collected, 
		only that particular fields are strings and others are integers, the tests. """
		
		self.my_data.collect()

		self.assertTrue(self.my_data.name.isalpha() and len(self.my_data.name) >= 4)
		self.assertTrue(self.my_data.hourly_rate.replace('.', '').isdigit() and 
						float(self.my_data.hourly_rate) > 0) 
		self.assertTrue(self.my_data.date_available.isdigit() and self.my_data.date_available >= 1 and self.my_data.date_available <= 7)


	def test_summarize(self):
		""" Collect data, run the summarize function and get a JSON string back.
		Convert the JSON string to an object, where we then can test different
		items, for example that we expect that there is a 'name' field in the
		JSON object and that particular field is a string (without any numbers). """
		
		self.my_data.collect()
		summary = self.my_data.summarize()
		json_summary = json.loads(summary)

		self.assertTrue("name" in json_summary)
		self.assertTrue("hourly_rate" in json_summary)
		self.assertTrue("date_available" in json_summary)

		self.assertTrue(len(json_summary["name"]) >= 4)
		self.assertTrue(json_summary["hourly_rate"].replace(",", "").isdigit() and float(json_summary["hourly_rate"] > 0))
		self.assertTrue(json_summary["date_available"] >= 1 and json_summary["date_available"] <= 7) 

if __name__ == "__main__":
	unittest.main()