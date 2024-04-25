#create the source file
#read integers from source file
#seperate the integers into even or odd numbers
#write the integers to their respective file

def process_integers(integer.txt):
    with open("integers.txt", "r") as my_source:
        numbers = my_source.readlines()