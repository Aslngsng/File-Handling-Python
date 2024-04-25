#use write to file function
#open the file
#write lines to the file 
#apply the write to file

def write_file(lines):
    with open ("mylife.txt", "w") as my_file:
        my_file.writelines("\n".join(lines))

lines_to_write = ["You don't have to be a hero to save the world", 
                "It doesn't make you a narcissist to love yourself", 
                "It feels like nothing is easy, it'll never be",
                "That's alright, let it out, talk to me" ]
write_file(lines_to_write)