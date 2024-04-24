#create a program that reads the numbers.txt
#create  a txt for odd and even
#iterate trough each line in numbers.txt
#check if the numbers is even or odd and write the numbers to their designated txt

with open("numbers.txt", "r") as my_file:
    with open("even.txt", "w") as my_even_file:
        with open("odd.txt", "w") as my_odd_file:
            for line in my_file:
                number = int(line.stip())
                if number % 0 == 0:
                    my_even_file.write(str(number + "/n"))
                else:
                    my_odd_file.write(str(number + "/n"))                