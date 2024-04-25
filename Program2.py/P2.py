#read the data from the class.txt
#compare the GWAs of the students to find the highest GWA
#print the student who has highest GWA, including their GWA


with open("class_data.txt", "r") as my_class_data:
    lines = my_class_data.readlines()

highest_GWA = 0.0
highest_student_GWA = ""
for line in lines:
    student_data = line.strip().split(",")
    if len (student_data) <2:
        continue
    student_name = student_data[0]
    GWA = float(student_data[1])
    if GWA >= highest_GWA:
        highest_GWA = GWA
        highest_student_GWA = student_name
print("The student(s) with highest GWA: " + highest_student_GWA + ", with GWA of " + str(highest_GWA))