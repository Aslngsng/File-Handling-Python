#use write to file function
#open the file
#write lines to the file 
#apply the write to file

def write_file(lines):
    with open ("mylife.txt", "w") as my_file:
        my_file.writelines("\n".join(lines))