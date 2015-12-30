from selenium import webdriver
import unittest 

class NewVisitorTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()		
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith heard about this cool to-do app. 
		# She goes to check out its homepage:
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention 'To-do' lists:
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to enter a to-do item:

		# She types 'buy peacock feathers' into a text box.
		# Her hobby is tying fly-fishing lures

		# When she hits 'enter', the page updates, and lists
		# '1. buy peacock feathers' as an item in the to-do list. 

		# There is still a text box inviting her to add another item
		# She enters 'Use peacock feathers to make a fly'

		# the page updates again, and now shows both items on her list 

		# Edith wonders if the site will remember her list. Then she sees 
		# that the site has generated a unique URL for her. There is some
		# explanatory text 

		# She visits that URL. The list is still there. 

		# Satisfied, she goes back to sleep. 

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')