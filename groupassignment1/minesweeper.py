"""
This is a program that read two numbers from a file that specifies the lines and columns of a following two dimensional list,
and then write it to another file to show a number in a square which tells you how many mines there are adjacent to that square.
"""


class Minesweeper:
    def __init__(self, input_location, output_location):
        self.input_location = input_location
        self.output_location = output_location
        self.input_file=open(self.input_location, "r")
        self.output_file=open(self.output_location, "w")


    def close_input_file(self):
        self.input_file.close()

    def close_output_file(self):
        self.output_file.close()

    def build_hints_map(self, int1, int2, input_file):
        arraylist = [[0 for m in range(int2)] for n in range(int1)]
        for n in range(int1):
            single_line = input_file.readline().strip("\n")
            for m, val in enumerate(single_line):
                if val == "*":
                    arraylist[n][m] = "*"
                    if n - 1 >= 0 and m - 1 >= 0 and arraylist[n - 1][m - 1] != "*":
                        arraylist[n - 1][m - 1] += 1
                    if n - 1 >= 0 and arraylist[n - 1][m] != "*":
                        arraylist[n - 1][m] += 1
                    if n - 1 >= 0 and m + 1 <= int2 - 1 and arraylist[n - 1][m + 1] != "*":
                        arraylist[n - 1][m + 1] += 1
                    if m - 1 >= 0 and arraylist[n][m - 1] != "*":
                        arraylist[n][m - 1] += 1
                    if m + 1 <= int2 - 1 and arraylist[n][m + 1] != "*":
                        arraylist[n][m + 1] += 1
                    if n + 1 <= int1 - 1 and m - 1 >= 0 and arraylist[n + 1][m - 1] != "*":
                        arraylist[n + 1][m - 1] += 1
                    if n + 1 <= int1 - 1 and arraylist[n + 1][m] != "*":
                        arraylist[n + 1][m] += 1
                    if n + 1 <= int1 - 1 and m + 1 <= int2 - 1 and arraylist[n + 1][m + 1] != "*":
                        arraylist[n + 1][m + 1] += 1
        return arraylist

    def compute_result(self):
        int1, int2 = self.input_file.readline().split()
        count = 1
        while int(int1) != 0:
            int1 = int(int1)
            int2 = int(int2)
            self.output_file.write("Field #" + str(count) + ":" + "\n")
            array_map = self.build_hints_map(int1, int2, self.input_file)
            for line in array_map:
                for char in line:
                    self.output_file.write(str(char))
                self.output_file.write("\n")
            self.output_file.write("\n")
            count += 1
            int1, int2 = self.input_file.readline().split()
        self.close_input_file()
        self.close_output_file()



#
# # open file for input (reading mode)
# input_file = open("mines.txt", "r")
#
# # open file for output (writing mode)
# output_file = open("minesweeper_output.txt", "w")
#
# # grab first line of input from file which should be two numbers
# int1, int2 = input_file.readline().split()
#
# count = 1
# while int(int1) != 0:
#     int1 = int(int1)
#     int2 = int(int2)
#     output_file.write("Field #" + str(count) + ":" + "\n")
#     arraylist = [[0 for m in range(int2)] for n in range(int1)]
#     for n in range(int1):
#         line = input_file.readline().strip("\n")
#         for m, char in enumerate(line):
#             if char == "*":
#                 arraylist[n][m] = "*"
#                 if n - 1 >= 0 and m - 1 >= 0 and arraylist[n - 1][m - 1] != "*":
#                     arraylist[n - 1][m - 1] += 1
#                 if n - 1 >= 0 and arraylist[n - 1][m] != "*":
#                     arraylist[n - 1][m] += 1
#                 if n - 1 >= 0 and m + 1 <= int2 - 1 and arraylist[n - 1][m + 1] != "*":
#                     arraylist[n - 1][m + 1] += 1
#                 if m - 1 >= 0 and arraylist[n][m - 1] != "*":
#                     arraylist[n][m - 1] += 1
#                 if m + 1 <= int2 - 1 and arraylist[n][m + 1] != "*":
#                     arraylist[n][m + 1] += 1
#                 if n + 1 <= int1 - 1 and m - 1 >= 0 and arraylist[n + 1][m - 1] != "*":
#                     arraylist[n + 1][m - 1] += 1
#                 if n + 1 <= int1 - 1 and arraylist[n + 1][m] != "*":
#                     arraylist[n + 1][m] += 1
#                 if n + 1 <= int1 - 1 and m + 1 <= int2 - 1 and arraylist[n + 1][m + 1] != "*":
#                     arraylist[n + 1][m + 1] += 1
#     for line in arraylist:
#         for char in line:
#             output_file.write(str(char))
#         output_file.write("\n")
#     output_file.write("\n")
#     count += 1
#     int1, int2 = input_file.readline().split()
#
# # close files!
# input_file.close()
# output_file.close()
