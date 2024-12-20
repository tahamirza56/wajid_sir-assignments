# could not do it myself, took some help from chatgpt
def calculate_averages(students):
    for student in students:
        name = student['name']
        scores = student['scores']
        average_score = sum(scores) / len(scores) if scores else 0
        print(f"Average score for {name}: {average_score:.2f}")


def find_highest_avg_student(students):
    highest_avg = -1
    best_student = None

    for student in students:
        name = student['name']
        scores = student['scores']
        average_score = sum(scores) / len(scores) if scores else 0

        if average_score > highest_avg:
            highest_avg = average_score
            best_student = name

    print(f"Student with the highest average score: {best_student} with an average score of {highest_avg:.2f}")

students = [
    {"name": "taha", "scores": (85, 92, 78, 88,)},
    {"name": "arsalan", "scores": (75, 80, 85, 90,)},
    {"name": "jibran", "scores": (95, 97, 99, 93,)},
    {"name": "ali", "scores": (80, 85, 84, 82,)}
]
calculate_averages(students)
find_highest_avg_student(students)
