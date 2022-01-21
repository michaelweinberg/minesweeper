import unittest
from minesweeper import Minesweeper


class MinesweeperTest(unittest.TestCase):

    def test_first_line_bad_input(self):
        """it should fail if given an input that is not a number"""
        input_file = open("bad_input.txt", "r")
        int1, int2 = input_file.readline().split()
        # self.assertRaises(ValueError, int(int2))
        self.assertFalse(int2.isnumeric())
        input_file.close()


    def test_first_line_good_input(self):
        """it should read the first line of the input file and use the two numbers to create a grid"""
        input_file = open("simple_input.txt", "r")
        int1, int2 = input_file.readline().split()
        self.assertEqual(int(int1), 4)
        self.assertEqual(int(int2), 5)
        input_file.close()

    def test_hints_length(self):
        """it should return a minesweeper map of length the same as  the first number in the first line"""
        minesweeper = Minesweeper()
        input_file = open("simple_input.txt", "r")
        int1, int2 = input_file.readline().split()
        hint_list = minesweeper.build_hints_map(int1, int2, input_file)
        self.assertEqual(len(hint_list), 4)
        input_file.close()

    def test_read_lines(self):
        """it should read a mine from the second line of the input file if it's there"""
        minesweeper = Minesweeper()
        input_file = open("simple_input.txt", "r")
        int1, int2 = input_file.readline().split()
        hint_list = minesweeper.build_hints_map(int1, int2, input_file)
        self.assertEqual(hint_list[0][0], "*")
        self.assertEqual(hint_list[0][1], 1)
        self.assertEqual(hint_list[0][2], 0)
        self.assertEqual(hint_list[0][3], 0)
        self.assertEqual(hint_list[0][4], 0)
        input_file.close()

    def test_hints_zero_length(self):
        """it should return an empty array if given an input of 0 0"""
        minesweeper = Minesweeper()
        input_file = open("zero_input.txt", "r")
        int1, int2 = input_file.readline().split()
        hint_list = minesweeper.build_hints_map(int1, int2, input_file)
        self.assertEqual(len(hint_list), 0)
        input_file.close()

if __name__ == '__main__':
    unittest.main()

    # *100
    # 2210
    # 1 * 10
    # 1110