import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import verify_link

class TestMain(unittest.TestCase):
    
    def test_invalid_number_arguments(self) -> None:        
        incorrect_base_url = "https://www.dummy.com/"

        with self.assertRaises(ValueError) as context:
            verify_link(incorrect_base_url)
        
        self.assertEqual(str(context.exception), incorrect_base_url + " is not a valid youtube media link.")

unittest.main()
