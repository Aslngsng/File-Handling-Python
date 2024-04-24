#create a program that reads the numbers.txt
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        print(line.strip)