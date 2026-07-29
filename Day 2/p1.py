# Program to calculate the attendence percentage of a student and eligibility for exams based on the attendance.

total_classes = 210
attended_classes = int(input("Enter the number of classes attended: "))

attendence_percentage = (attended_classes / total_classes) * 100

print("Attendance Percentage of the student is : {:.2f}%".format(attendence_percentage))

if attendence_percentage>=70:
    print("Student is eligible for exams")
    
else:
    print("Student is not eligible for the exam.")
    
    