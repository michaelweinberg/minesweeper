from random import randint

#open file for output (writing mode)
output_file = open('minesweeper_generator_output.txt', 'w')

#randomly determine number of mine fields to print out
number_of_fields = randint(1, 100)
for f in range(0, number_of_fields):
    #write to output file row and column of field
    #first, randomly generate two integers both between 1 and 100 inclusive for row and column values
    row = randint(1, 100)
    column = randint(1, 100)
    output_file.write(str(row) + " " + str(column) + "\n")
    print(row, column)

    #next, randomly output * or . depending on pre-determined chance of mine
    chance_of_mine = randint(0, 100)
    for n in range(0, int(row)):
        counter = 0
        for m in range(0, int(column)):
            #chance of individual output being a mine
            chance = randint(0, 100)

            if chance <= chance_of_mine:
                print("*")
                output_file.write("*")
                counter += 1
                if counter % int(column) == 0:
                    output_file.write("\n")
            else:
                print(".")
                output_file.write(".")
                counter += 1
                if counter % int(column) == 0:
                    output_file.write("\n")
        print(int(counter))
output_file.write("0 0" + "\n")
