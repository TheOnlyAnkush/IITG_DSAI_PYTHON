#Main Programe to get student details and marks.

def cal_grade(score):
    if score >= 90:
        return  "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C" 
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"
    

def grade_card():
    #Taking student and marks as input
    print("--------------------------")
    student_name = input("Enter Student Name: ")
    roll_no = input("Enter Roll No.: ")
    maths_marks = int(input("Enter marks in Maths: "))
    physics_marks = int(input ("Enter marks in Physics: "))
    chemistry_marks = int(input ("Enter marks in Chemistry: "))
    print("--------------------------")
   
    #Calculation of grades for each subject
    maths_grade = cal_grade(maths_marks)
    physics_grade = cal_grade(physics_marks)
    chemistry_grade = cal_grade(chemistry_marks)    
    
    # Calculating overall grade based on average marks
    average_marks = (maths_marks + physics_marks + chemistry_marks) / 3
    overall_grade = cal_grade(average_marks)

    # Printing the grade card
    print("Here is the Grade Card:")
    print("--------------------------")
    print("Student Name: ", student_name)
    print("Student Roll: ", roll_no)
    print("Grade in Maths: ", maths_grade)
    print("Grades in Physics: ", physics_grade)
    print("Grades in Chemistry: ", chemistry_grade)
    print("Overall Grade: ", overall_grade)
    print("--------------------------")

#Call the function to generate the grade card
grade_card()