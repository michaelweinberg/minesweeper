import unittest
import os


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

        cmd = 'main.py'

        os.system(cmd)

        output_file = open('test_output.txt', "r")
        self.assertEqual('Field #1:\n', output_file.readline(), "Did not output 'Field #1:")
        self.assertEqual('*100\n', output_file.readline(), "Did not output '*100'")
        self.assertEqual('2210\n', output_file.readline(), "Did not output '2210'")
        self.assertEqual('1*10\n', output_file.readline(), "Did not output '1*10'")
        self.assertEqual('1110\n', output_file.readline(), "Did not output '1110'")


if __name__ == '__main__':
    unittest.main()
