import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import validator
from main import OPTIONS_LIST

class TestValidator(unittest.TestCase):
    def __init__(self,  *args, **kwargs) -> None:
        super(TestValidator, self).__init__(*args, **kwargs)
        self.validator = validator.Validator(OPTIONS_LIST)

    
    def test_invalid_number_arguments(self) -> None:        
        argv = ["py", "text.txt"]

        with self.assertRaises(ValueError) as context:
            self.validator.invalid_number_arguments(argv)
        
        self.assertEqual(str(context.exception), "Invalid number of arguments.")

    def test_invalid_extension(self) -> None:
        text_file_path = "text.js"

        with self.assertRaises(ValueError) as context:
            self.validator.invalid_extension(text_file_path)
        
        self.assertEqual(str(context.exception), "It seems that the file you gave is not a .txt file.")

    def test_unexistant_file(self) -> None:
        text_file_path = "text.txt"

        with self.assertRaises(ValueError) as context:
            self.validator.unexistant_file(text_file_path)
        
        self.assertEqual(str(context.exception), "The .txt file you gave does not exist.")

    def test_invalid_option(self) -> None:
        argv = ["py", "text.txt", "unexistant_option"]

        with self.assertRaises(ValueError) as context:
            self.validator.invalid_option(argv)
        
        self.assertEqual(str(context.exception), "The options you gave is invalid (valid options : single_video, single_audio, playlist_video, playlist_audio).")

unittest.main()
