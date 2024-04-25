#create the source file
#read integers from source file
#seperate the integers into even or odd numbers
#write the integers to their respective file

def process_integers(integer.txt):
    with open("integers.txt", "r") as my_source:
        numbers = my_source.readlines()

    squared_even = []
    cube_odd = []
    for num in numbers:
        num = int(num.strip())
        if num % 2 == 0:
            squared_even.append(num ** 2)
        else:
            cube_odd.append(num ** 3)
            