import unittest
from util import validate_reference, UserInputError
from datetime import datetime

class TestReferenceValidation(unittest.TestCase):
    def setUp(self):
        self.title = "Test Title"
        self.author = "Teppo Test"
        self.year = 2024
        self.current_year = datetime.now().year
        self.reference_type = "book"
    
    def test_valid_book_reference_does_not_raise_error(self):
        self.assertEqual(validate_reference(self.title, self.author, self.year, self.reference_type), True)

    def test_valid_article_reference_does_not_raise_error(self):
        self.assertEqual(validate_reference(self.title, self.author, self.year, "article"), True)
        self.assertEqual(validate_reference(self.title, self.author, self.year, "article", journal="Journal of testing", volume="32", pages="87-133"), True)

    def test_valid_inproceedings_reference_does_not_raise_error(self):
        self.assertEqual(validate_reference(self.title, self.author, self.year, "inproceedings"), True)
        self.assertEqual(validate_reference(self.title, self.author, self.year, "inproceedings", booktitle="Title of Testbook"), True)

    def test_empty_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference("", self.author, self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Teos\" ei voi olla tyhjä")

    def test_only_a_space_in_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(" ", self.author, self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Teos\" ei voi olla tyhjä")

    def test_none_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(None, self.author, self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Teos\" ei voi olla tyhjä")

    def test_too_long_title_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference("A" * 101, self.author, self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Teos\" maksimipituus on 100 merkkiä")

    def test_empty_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, "", self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Kirjoittanut\" ei voi olla tyhjä")

    def test_only_a_space_in_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, " ", self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Kirjoittanut\" ei voi olla tyhjä")

    def test_none_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, None, self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Kirjoittanut\" ei voi olla tyhjä")

    def test_too_long_author_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, "A" * 101, self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Kirjoittanut\" maksimipituus on 100 merkkiä")
    
    def test_special_characters_in_author_dont_raises_an_error(self):
        self.assertEqual(validate_reference(self.title, "Teppå Test'sÅäÄöÖ", self.year, self.reference_type), True)

    def test_forbidden_character_in_author_raises_an_error(self):
        self.assertEqual(validate_reference(self.title, "Teppå Test'sÅäÄöÖ", self.year, self.reference_type), True)
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, "Teppo Test!", self.year, self.reference_type)
        self.assertEqual(str(error.exception), "\"Kirjoittanut\" sisältää virheellisiä merkkejä")

    def test_empty_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, "", self.reference_type)
        self.assertEqual(str(error.exception), "\"Painovuosi\" tulee esittää numeroina")

    def test_only_a_space_in_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, " ", self.reference_type)
        self.assertEqual(str(error.exception), "\"Painovuosi\" tulee esittää numeroina")

    def test_none_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, None, self.reference_type)
        self.assertEqual(str(error.exception), "\"Painovuosi\" tulee esittää numeroina")

    def test_too_small_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, "999", self.reference_type)
        self.assertEqual(str(error.exception), f"\"Painovuosi\" tulee olla 1000-{self.current_year} väliltä")

    def test_too_big_year_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, str(self.current_year + 1), self.reference_type)
        self.assertEqual(str(error.exception), f"\"Painovuosi\" tulee olla 1000-{self.current_year} väliltä")

    def test_only_a_space_in_journal_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "article", journal=" ")
        self.assertEqual(str(error.exception), "\"Lehti\" ei voi olla pelkkiä välilyöntejä")

    def test_too_long_journal_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "article", journal="A" * 101)
        self.assertEqual(str(error.exception), "\"Lehti\" maksimipituus on 100 merkkiä")
        
    def test_only_a_space_in_volume_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "article", volume=" ")
        self.assertEqual(str(error.exception), "\"Volyymi\" ei voi olla pelkkiä välilyöntejä")

    def test_too_long_volume_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "article", volume="A" * 11)
        self.assertEqual(str(error.exception), "\"Volyymi\" tulee olla 1-10 merkkiä")

    def test_incorrect_page_number_format_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "article", pages="30 54")
        self.assertEqual(str(error.exception), "\"Sivut\" on virheellisessä formaatissa")

    def test_too_long_page_number_input_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "article", pages="10527-10758")
        self.assertEqual(str(error.exception), "\"Sivut\" tulee olla 1-10 merkkiä")

    def test_correct_page_number_format_does_not_raise_an_error(self):
        self.assertEqual(validate_reference(self.title, self.author, self.year, "article", pages="30–54"), True)
        self.assertEqual(validate_reference(self.title, self.author, self.year, "article", pages="30-54"), True)
        self.assertEqual(validate_reference(self.title, self.author, self.year, "article", pages="1000-1215"), True)

    def test_only_a_space_in_booktitle_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "inproceedings", booktitle=" ")
        self.assertEqual(str(error.exception), "\"Kirjaotsikko\" ei voi olla pelkkiä välilyöntejä")

    def test_too_long_booktitle_raises_an_error(self):
        with self.assertRaises(UserInputError) as error:
            validate_reference(self.title, self.author, self.year, "inproceedings", booktitle="A" * 101)
        self.assertEqual(str(error.exception), "\"Kirjaotsikko\" maksimipituus on 100 merkkiä")