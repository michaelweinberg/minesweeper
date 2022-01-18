"""
This is a program that read two numbers from a file that specifies the lines and columns of a following two dimensional list,
and then write it to another file to show a number in a square which tells you how many mines there are adjacent to that square.
"""

# open file for input (reading mode)
input_file = open("mines.txt", "r")

# open file for output (writing mode)
output_file = open("minesweeper_output.txt", "w")

# grab first line of input from file which should be two numbers
int1, int2 = input_file.readline().split()

count = 1
while int(int1) != 0:
    int1 = int(int1)
    int2 = int(int2)
    output_file.write("Field #" + str(count) + ":" + "\n")
    arraylist = [[0 for m in range(int2)] for n in range(int1)]
    for n in range(int1):
        line = input_file.readline().strip("\n")
        for m, char in enumerate(line):
            if char == "*":
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
    for line in arraylist:
        for char in line:
            output_file.write(str(char))
        output_file.write("\n")
    output_file.write("\n")
    count += 1
    int1, int2 = input_file.readline().split()

# close files!
input_file.close()
output_file.close()
