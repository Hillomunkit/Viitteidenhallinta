import unittest
from util import validate_reference, UserInputError
from datetime import datetime

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        self.title = "Test Title"
        self.author = "Teppo Test"
        self.year = 2024
        self.current_year = datetime.now().year
    
    def test_valid_user_input_does_not_raise_error(self):
        self.assertEqual(validate_reference(self.title, self.author, self.year), True)

    def test_empty_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference("", self.author, self.year)
        self.assertEqual(str(error.exception), "Title can't be empty")

    def test_only_a_space_in_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(" ", self.author, self.year)
        self.assertEqual(str(error.exception), "Title can't be empty")

    def test_none_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(None, self.author, self.year)
        self.assertEqual(str(error.exception), "Title can't be empty")

    def test_too_long_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference("A" * 101, self.author, self.year)
        self.assertEqual(str(error.exception), "Maximum title length is 100 characters")

    def test_empty_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, "", self.year)
        self.assertEqual(str(error.exception), "Author can't be empty")

    def test_only_a_space_in_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, " ", self.year)
        self.assertEqual(str(error.exception), "Author can't be empty")

    def test_none_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, None, self.year)
        self.assertEqual(str(error.exception), "Author can't be empty")

    def test_too_long_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, "A" * 101, self.year)
        self.assertEqual(str(error.exception), "Maximum author length is 100 characters")
    
    def test_special_characters_in_author_dont_raises_an_error(self):
        self.assertEqual(validate_reference(self.title, "Teppå Test'sÅäÄöÖ", self.year), True)

    def test_forbidden_character_in_author_raises_an_error(self):
        self.assertEqual(validate_reference(self.title, "Teppå Test'sÅäÄöÖ", self.year), True)
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, "Teppo Test!", self.year)
        self.assertEqual(str(error.exception), "Author name contains invalid characters")

    def test_empty_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, "")
        self.assertEqual(str(error.exception), "Year must be a valid integer")

    def test_only_a_space_in_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, " ")
        self.assertEqual(str(error.exception), "Year must be a valid integer")

    def test_none_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, None)
        self.assertEqual(str(error.exception), "Year must be a valid integer")

    def test_too_small_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, 999)
        self.assertEqual(str(error.exception), f"Year must be between 1000 and {self.current_year}")

    def test_too_big_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.current_year + 1)
        self.assertEqual(str(error.exception), f"Year must be between 1000 and {self.current_year}")