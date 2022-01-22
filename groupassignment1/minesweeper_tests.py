import unittest
from minesweeper import Minesweeper



class MinesweeperTests(unittest.TestCase):
    """ This class tests that output for a given minefield is formatted properly.
    """

    def test_output_format(self):
        """ Does output first read "Field #n:" where n is the minefield currently being processed?
            Is rest of output accurate for the minefield read in?
        """
        input_file = open('input.txt', "w")
        input_file.write("4 4\n")
        input_file.write("*...\n")
        input_file.write("....\n")
        input_file.write(".*..\n")
        input_file.write("....\n")
        input_file.write("0 0\n")

        input_file.close()

        minesweeper = Minesweeper('input.txt', 'test_output.txt')
        minesweeper.compute_result()
        output_file = open('test_output.txt', "r")
        self.assertEqual('Field #1:\n', output_file.readline(), "Did not output 'Field #1:")
        self.assertEqual('*100\n', output_file.readline(), "Did not output '*100'")
        self.assertEqual('2210\n', output_file.readline(), "Did not output '2210'")
        self.assertEqual('1*10\n', output_file.readline(), "Did not output '1*10'")
        self.assertEqual('1110\n', output_file.readline(), "Did not output '1110'")
        output_file.close()

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
        minesweeper = Minesweeper("simple_input.txt", "simple_output.txt")
        input_file = open("simple_input.txt", "r")
        int1, int2 = input_file.readline().split()
        hint_list = minesweeper.build_hints_map(int(int1), int(int2), input_file)
        self.assertEqual(len(hint_list), 4)
        input_file.close()
        minesweeper.close_output_file()
        minesweeper.close_input_file()

    def test_read_lines(self):
        """it should read a mine from the second line of the input file if it's there"""
        minesweeper = Minesweeper("simple_input.txt", "simple_output.txt")
        input_file = open("simple_input.txt", "r")
        int1, int2 = input_file.readline().split()
        hint_list = minesweeper.build_hints_map(int(int1), int(int2), input_file)
        self.assertEqual(hint_list[0][0], "*")
        self.assertEqual(hint_list[0][1], 1)
        self.assertEqual(hint_list[0][2], 0)
        self.assertEqual(hint_list[0][3], 0)
        self.assertEqual(hint_list[0][4], 0)
        input_file.close()
        minesweeper.close_output_file()
        minesweeper.close_input_file()

    def test_hints_zero_length(self):
        """it should return an empty array if given an input of 0 0"""
        input_file = open("zero_input.txt", "r")
        minesweeper = Minesweeper("zero_input.txt", "zero_output.txt")
        int1, int2 = input_file.readline().split()
        hint_list = minesweeper.build_hints_map(int(int1), int(int2), input_file)
        self.assertEqual(len(hint_list), 0)
        input_file.close()
        minesweeper.close_output_file()
        minesweeper.close_input_file()

if __name__ == '__main__':
    unittest.main()
