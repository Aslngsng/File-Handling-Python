#create a program that reads the numbers.txt
#create  a txt for odd and even
#iterate trough each line in numbers.txt
#check if the numbers is even or odd and write the numbers to their designated txt

def read_write():
    with open("numbers.txt", "r") as my_file:
      for line in my_file:
        if int(line) % 2 == 0:
            with open("even.txt", "a") as my_even_file:
                my_even_file.write(str(line) + "\n")
        else:
            with open("odd.txt", "a") as my_odd_file:
                    my_odd_file.write(str(line) + "\n")

read_write()
        