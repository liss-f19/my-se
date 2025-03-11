import unittest
from calculator import get_number_input

class TestCalculator(unittest.TestCase):

    def test_empty_string(self):
        # Given: empty str
        str_in = ""
        expected = 0

        # When: the function is called
        result = get_number_input(str_in)

        # Then: 0
        self.assertEqual(result, expected)

    def test_single_num(self):
        # Given: single num
        str_in = "5"
        expected = 5

        # When: the function is called
        result = get_number_input(str_in)

        # Then: number
        self.assertEqual(result, expected)

    def test_two_comma_delimited(self):
        # Given: two nums with comma between
        str_in = "5,3"
        expected = 8

        # When: the function is called
        result = get_number_input(str_in)

        # Then: 8
        self.assertEqual(result, expected)

    def test_two_newline_delimited(self):
        # Given: two nums with \n between
        str_in = "5\n3"
        expected = 8

        # When: The function is called
        result = get_number_input(str_in)

        # Then: 8
        self.assertEqual(result, expected)

    def test_three_numbers_delimited(self):
        # two nums with comma and \n
        str_in = "1,2\n3"
        expected = 6

        # When: the function is called
        result = get_number_input(str_in)

        # Then: 6
        self.assertEqual(result, expected)

    def test_negative_values(self):
        # Given: negative
        str_in = "-5\n3"

        # When: The function is called
        # Then: val err
        with self.assertRaises(ValueError) as context:
            get_number_input(str_in)

        self.assertEqual(str(context.exception), "Invalid input! Please enter valid numbers.")

    def test_numbers_greater_than_1000_are_ignored(self):
        # Given: num >1000
        str_in = "2,1001"
        expected = 2  

        # When: The function is called
        result = get_number_input(str_in)

        # Then: ignored 1001 and just 2 as output
        self.assertEqual(result, expected)

    def test_single_char_custom_delimiter(self):
        # Given: single-char custom delimiter
        str_in = "//#\n1#2"
        expected = 3

        # When: the function is called
        result = get_number_input(str_in)

        # Then: sum of 1 and 2
        self.assertEqual(result, expected)

    def test_multi_char_custom_delimiter(self):
        # Given: multi-char custom delimiter
        str_in = "//[###]\n1###2"
        expected = 3

        # When: the function is called
        result = get_number_input(str_in)

        # Then: sum of 1 and 2
        self.assertEqual(result, expected)

    def test_multiple_custom_delimiters(self):
        # Given: multiple customs del
        str_in = "//[*][%]\n1*2%3"
        expected = 6

        # When: the function is called
        result = get_number_input(str_in)

        # Then: sum of 1 2 3
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
