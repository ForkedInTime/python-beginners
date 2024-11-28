# 1) return a list of all students whose firstName begins with the character letter
def get_students_starting_with(students, letter):
   return [student for student in students if student[0].lower() == letter.lower()]  
    # example: get_students_starting_with(['Tanguy', 'Amine'], 'a') => ['Amine']


# 2) return the result obtained by student if:

# 2.a) you know its position in the results list
def get_score_position(results, index):
    return results[index][1]
    pass
    # example: get_score_position([["Tanguy", 5], ["Amine", 7]], 0) => 5


# 2.b) you don't know its position in the results list
def get_score_unknown_position(results, name):
    return next((result[1] for result in results if result[0] == name), None)
    pass
    # example: get_score_unknown_position([["Tanguy", 5], ["Amine", 7]], 'Amine') => 7


# 3) return an average of the mathematics's result of all students (suppose you don't know the list's length)
def average_math_result(results):
    return sum(result[1] for result in results) / len(results) if results else 0
    pass
    # example: get_average_math_result([["Tanguy", 5], ["Amine", 7]]) => 6


# 4) return a new list with all students who succeeded (>= 50%) mathematics
def student_who_succeeded(results):
    return [result[0] for result in results if result[1] >= 5]
    pass
    # example: student_who_succeeded([["Tanguy", 5], ["Amine", 7]]) => ['Tanguy', 'Amine']


# 5) return a new list with all student that didn't participate to the mathematics's exam
def not_participating(students, results):
    return [student for student in students if student not in [result[0] for result in results]]
    pass
    # example: not_participating(['Tanguy', 'Amine'], [["Tanguy", 5]]) => ['Amine']
