#create a program that reads the numbers.txt
#create  a txt for odd and even
#iterate trough each line in numbers.txt
#check if the numbers is even or odd and write the numbers to their designated txt

with open("numbers.txt", "r") as my_file:
    for line in my_file:
        line = line.strip
        print(line)
                       