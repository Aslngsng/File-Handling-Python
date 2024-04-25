#read the data from the class.txt
#compare the GWAs of the students to find the highest GWA
#print the student who has highest GWA, including their GWA


with open("class_data.txt", "r") as my_class_data:
    lines = my_class_data.readlines()
highest_GWA = 0.0
highest_student_GWAs = []

for line in lines:
    student_data = line.strip().split(",")
    student_name = student_data[0]
    GWA = float(student_data[1])
    if GWA > highest_GWA:
        highest_GWA = GWA
        highest_student_GWAs = [student_name]
    elif GWA == highest_GWA:
        highest_student_GWAs.append(student_name)

if len (highest_student_GWAs) == 1:
    print("The student with highest GWA: " + highest_student_GWAs[0] + ", with GWA of " + str(highest_GWA))
else:
    print("The number of students with highest GWA: " + ", ".join(highest_student_GWAs) + "with GWA of " + str(highest_GWA))