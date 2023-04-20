import unittest
from io import StringIO
from unittest.mock import patch

from maths import calculate

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.input1 = '5\n'
        self.input2 = '+\n'
        self.input3 = '2\n'
        self.input4 = 'q\n'
        self.expected_output_addition = 'Answer: 7\n'
        self.stdin_patch_addition = patch('sys.stdin', StringIO(self.input1 + self.input2 + self.input3 + self.input4))

        self.input1_sub = '10\n'
        self.input2_sub = '-\n'
        self.input3_sub = '3\n'
        self.input4_sub = 'q\n'
        self.expected_output_subtraction = 'Answer: 7\n'
        self.stdin_patch_subtraction = patch('sys.stdin', StringIO(self.input1_sub + self.input2_sub + self.input3_sub + self.input4_sub))

        self.input1_mul = '5\n'
        self.input2_mul = '*\n'
        self.input3_mul = '2\n'
        self.input4_mul = 'q\n'
        self.expected_output_multiplication = 'Answer: 10\n'
        self.stdin_patch_multiplication = patch('sys.stdin', StringIO(self.input1_mul + self.input2_mul + self.input3_mul + self.input4_mul))

        self.input1_div = '10\n'
        self.input2_div = '/\n'
        self.input3_div = '5\n'
        self.input4_div = 'q\n'
        self.expected_output_division = 'Answer: 2.0000000000\n'
        self.stdin_patch_division = patch('sys.stdin', StringIO(self.input1_div + self.input2_div + self.input3_div + self.input4_div))

    def test_calculate_addition(self):
        with self.stdin_patch_addition:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                calculate()
                self.assertEqual(fake_output.getvalue().strip(), self.expected_output_addition)

    def test_calculate_subtraction(self):
        with self.stdin_patch_subtraction:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                calculate()
                self.assertEqual(fake_output.getvalue().strip(), self.expected_output_subtraction)

    def test_calculate_multiplication(self):
        with self.stdin_patch_multiplication:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                calculate()
                self.assertEqual(fake_output.getvalue().strip(), self.expected_output_multiplication)

    def test_calculate_division(self):
        with self.stdin_patch_division:
            with patch('sys.stdout', new=StringIO()) as fake_output:
                calculate()
                self.assertEqual(fake_output.getvalue().strip(), self.expected_output_division)

if __name__ == '__main__':
    unittest.main()
