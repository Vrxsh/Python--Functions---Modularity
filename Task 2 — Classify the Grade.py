def classify_grades(averages):
    classified = {}
    
    # Define thresholds locally
    grade_A = 90
    grade_B = 75
    grade_C = 60
    
    for name, avg in averages.items():
        if avg >= grade_A:
            grade = "A"
        elif avg >= grade_B:
            grade = "B"
        elif avg >= grade_C:
            grade = "C"
        else:
            grade = "F"
        classified[name] = (avg, grade)
    
    return classified