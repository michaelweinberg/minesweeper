def split(word):
    """return an array of characters split from a string
    pulled this code from here: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
    """
    return [char for char in word]

def is_new_field(new_field):
    """return a carriage return regex is passed True"""
    if new_field == True:
        return "\n"
    return ""


def build_2d_array(list):
    """return a parsed 2 dimensional array with all non-mine tiles represented as the integer 0"""
    myList = []
    for i in range(len(list)):
        line_array = split(list[i])
        for j in range(len(line_array)):
            if line_array[j] == ".":
                line_array[j] = 0
        myList.append(line_array)
    return myList


def build_map(two_d_list):
    """Return a two dimensional array showing the
    number of mines present in a 3x3 area around the current cell - lots of room for improvement here.
    """
    for i in range(len(two_d_list)):
        for k in range(len(two_d_list[i])):
            if two_d_list[i][k] == "*":
                #increment to the left if free and exists
                if k < len(two_d_list[i]) and k >= 1 and two_d_list[i][k-1] is not None and two_d_list[i][k-1] != "*":
                    two_d_list[i][k - 1] += 1
                #increment to the right if free
                if k < len(two_d_list[i]) - 1 and two_d_list[i][k + 1] is not None and two_d_list[i][k + 1] != "*":
                    two_d_list[i][k + 1] += 1
                #increment below if free
                if i < len(two_d_list) - 1 and two_d_list[i + 1][k] is not None and two_d_list[i + 1][k] != "*":
                    two_d_list[i + 1][k] += 1
                #incrmeent above if free
                if i <= len(two_d_list) - 1 and i >= 1 and two_d_list[i - 1][k] is not None and two_d_list[i - 1][k] != "*":
                    two_d_list[i - 1][k] += 1
                #increment up and left if free
                if i <= len(two_d_list) - 1 and i >= 1 and k >= 1 and two_d_list[i - 1][k - 1] is not None and two_d_list[i-1][k-1] != "*":
                    two_d_list[i - 1][k - 1] += 1
                #increment up and right if free
                if i <= len(two_d_list) - 1 and k < len(two_d_list[i]) - 1 and i >= 1 and two_d_list[i - 1][k + 1] is not None and two_d_list[i - 1][k + 1] != "*":
                    two_d_list[i - 1][k + 1] += 1
                #increment down and left if free
                if i < len(two_d_list) - 1 and k >= 1 and i <= len(two_d_list) - 1 and two_d_list[i + 1][k -1] is not None and two_d_list[i + 1][k -1] != "*":
                    two_d_list[i + 1][k - 1] += 1
                #increment down and right if free
                if i < len(two_d_list) - 1 and k < len(two_d_list[i]) - 1 and two_d_list[i + 1][k + 1] is not None and two_d_list[i + 1][k + 1] != "*":
                    two_d_list[i + 1][k + 1] += 1
    #parse all tiles as strings before returning
    for m in range(len(two_d_list)):
        for n in range(len(two_d_list[m])):
            two_d_list[m][n] = str(two_d_list[m][n])
    return two_d_list

def write_tiles(my_map, file):
    for k in range(len(my_map)):
        file.write("".join(my_map[k]) + "\n")

def main():
    """Main function logic to read file input using while loop and output to specific location"""
    #define input and output location
    input_file = open('mines.txt', 'r')
    # input_file = open('simple_input.txt', 'r')
    output_file = open('minesweeper_output.txt', 'w')

    #initialize values to be reset in while loop
    first_line = input_file.readline().strip("\n")
    row_column_array = (first_line.split(" "))
    lines_to_read = row_column_array[0]
    square_list = []
    counter = 1
    new_field = False
    #while loop to parse lines from input file
    while lines_to_read != 0 and lines_to_read != "0":
        for i in range(int(lines_to_read)):
            data = input_file.readline().strip("\n")
            square_list.append(data)
        two_d_list = build_2d_array(square_list)
        my_map = build_map(two_d_list)

        # for k in range(len(my_map)):
        #     output_file.write("".join(my_map[k]) + "\n")
        row_column_array = (input_file.readline().strip("\n").split(" "))
        lines_to_read = row_column_array[0]
        if lines_to_read != 0 or lines_to_read != "0":
            output_file.write(is_new_field(new_field) + "Field #" + str(counter) + ":\n")
            write_tiles(my_map, output_file)
        new_field = True
        counter += 1
        square_list = []

main()