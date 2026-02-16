def calculate_grade(*scores, **adjustments):
    # Logic: Average of scores + sum of all bonus adjustments
    
    # Calculate base average from *args
    if not scores:
        return 0.0
    
    base_avg = sum(scores) / len(scores)
    
    # Calculate total bonus from **kwargs (**adjustments)
    # .values() gets the numbers (5, 10) and sum makes it 15
    total_bonus = sum(adjustments.values())
    
    final_grade = base_avg + total_bonus
    return final_grade

# Task 1: Student with scores 85, 90, 78 (no bonus)
grade1 = calculate_grade(85, 90, 78)
print(f"Final Grade: {grade1:.2f}%")



# Task 2: Student with scores 70, 65, 80 (attendance=5, project=10 bonus)
grade2 = calculate_grade(70, 65, 80, attendance=5, project=10)
print(f"Final Grade: {grade2:.2f}%")

