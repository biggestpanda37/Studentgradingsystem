def assign_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'D'
    elif score >= 40:
        return 'E'
    else:
        return 'F'

def student_grading_system():
    students = []
    total_score = 0

    num_students = int(input("Enter number of students: "))

    for i in range(num_students):
        name = input(f"\nEnter name of student {i+1}: ")
        score = float(input(f"Enter score for {name}: "))

        grade = assign_grade(score)
        students.append({'name': name, 'score': score, 'grade': grade})
        total_score += score

    # Display Results
    print("\nStudent Report:")
    print("{:<15} {:<10} {:<5}".format("Name", "Score", "Grade"))
    print("-" * 30)
    for student in students:
        print("{:<15} {:<10} {:<5}".format(student['name'], student['score'], student['grade']))

    # Class average
    average = total_score / num_students
    print("\nClass Average Score:", round(average, 2))
    print("Class Average Grade:", assign_grade(average))

# Run the program
student_grading_system()