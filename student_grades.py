# 1. Tuple - Subject names
subjects = ("Maths", "Science", "English")

# 2. List - Student names
student_names = ["Raj", "Priya", "Amit", "Sneha", "Karan"]


# 3. Dictionary - Marks for each student
grade_book = {
    "Raj": [85, 78, 90],
    "Priya": [92, 88, 85],
    "Amit": [70, 75, 68],
    "Sneha": [95, 90, 92],
    "Karan": [80, 82, 78]
}

# 4. Set - To store unique grades
unique_grades = set()

def getgrade(avg): # Determine and store unique grades

  if avg >= 85: 
    grade = 'A'
  elif avg >= 70: 
     grade = 'B'
  elif avg < 70: 
     grade = 'C'

  unique_grades.add(grade)
  return grade

def analyze_grades():
    # Displaying all student names
    print(f"All Students: {student_names}")

    # Printing first 3 students using slicing
    print(f"First 3 Students: {student_names[:3]}")
    print("-" * 30)

    top_avg = 0
    top_student = ""

    for name in student_names:
        marks = grade_book[name]
        
        # Calculating average
        avg = sum(marks) / len(marks)
        print(f"{name}'s Average: {avg:.2f} - Grade: {getgrade(avg)}")

        # finding top scorer
        if avg > top_avg:
            top_avg = avg
            top_student = name

    

    print("-" * 30)
    # Finding student with highest average
    print(f"Top Scorer: {top_student} with an average of {top_avg:.2f}")

    # Printing all unique grades
    print(f"Unique Grades in Class: {sorted(unique_grades)}")

if __name__ == "__main__":
    analyze_grades()