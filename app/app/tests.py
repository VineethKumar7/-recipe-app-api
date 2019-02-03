from django.test import TestCase
# We are importing the function that we created.
from app.calc import add

# Then we create the test class.
class CalcTests(TestCase):
    # Just like test file all the test functions should begin with test.
    # If it don't start with test then it wont run the test.
    def test_add_numbers(self):
        # We always start a test with description of what you are testing.
        """Test that two numbers are added together"""
        # The test is composed of two stages.
            #Setup stage: where the function is tested
            #Assertion : where we test the output.
        self.assertEqual(add(3,8), 11)
    
