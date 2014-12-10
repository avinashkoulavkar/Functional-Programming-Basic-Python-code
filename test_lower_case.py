import unittest
from lower_case import to_lower

class LowerTestCase(unittest.TestCase):
	
	#test to verify data with number
	def test_for_number(self):
		self.assertFalse(to_lower('Avinash123'),msg='Need to validate for Number')

	#test if it convert to upper to lower
	def test_upper_to_lower(self):
		self.assertTrue(to_lower('AVINASH'))
	
	#test to verify it shows error when empty string
	def test_for_empty(self):
		self.assertFalse(to_lower(''),msg='Need to care about empty string')
		
if __name__=='__main__':
	unittest.main()
