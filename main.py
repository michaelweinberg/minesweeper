#open file for input (reading mode)
input_file = open('mines.txt', 'r')

#open file for output (writing mode)
output_file = open('minesweeper_output.txt', 'w')

#grab first line of input from file
field_number = 1
lines_to_read = str(input_file.readline().strip('\n'))

while lines_to_read != '0 0':
    print('current number of (rows, columns) is:', lines_to_read)
    (row, column) = lines_to_read.split()
    a = []
    for i in range(0, int(row)):
        a.append([str(j) for j in input_file.readline().split()][0])
        while i == int(row)-1:
            print(a)
            break

    #write to output file
    output_file.write("Field #" + str(field_number) + ":\n")
    counter = 0
    for n in range(0, int(row)):
        for m in range(0, int(column)):
            if a[n][m] == '*':
                output_file.write("*")
            else:
                if m > 0:
                    if a[n][m - 1] == '*':
                        counter += 1
                if m != int(column) - 1:
                    if a[n][m + 1] == '*':
                        counter += 1
                if n > 0:
                    if a[n - 1][m] == '*':
                        counter += 1
                if n != int(row) - 1:
                    if a[n + 1][m] == '*':
                        counter += 1
                if n > 0 and m != int(column) - 1:
                    if a[n - 1][m + 1] == '*':
                        counter += 1
                if n > 0 and m > 0:
                    if a[n - 1][m - 1] == '*':
                        counter += 1
                if n != int(row) - 1 and m > 0:
                    if a[n + 1][m - 1] == '*':
                        counter += 1
                if n != int(row) - 1 and m != int(column) - 1:
                    if a[n + 1][m + 1] == '*':
                        counter += 1
                output_file.write(str(counter))
                counter = 0
        output_file.write('\n')
    field_number += 1
    lines_to_read = str(input_file.readline().strip('\n'))

input_file.close()
print('done reading from file')
output_file.close()
