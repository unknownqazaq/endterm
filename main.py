# Function to convert letter grades to points
def convert_letter_to_points(*letters):
    grade_points = {
        'A+': 4.3, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7
    }
    return [grade_points[letter] for letter in letters]

# Function to convert percentage scores to points
def convert_percentage_to_points(*percentages):
    letter_grades = convert_letter_to_points('A+', 'D', 'C-', 'A-')
    return [letter_grades[int((percentage - 45) / 5)] for percentage in percentages]

# Function to calculate overall GPA
def calculate_gpa(*args):
    points = args[::2]
    credits = args[1::2]
    return sum([point * credit for point, credit in zip(points, credits)]) / sum(credits)


def read_grades(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]

def calculate_and_save_gpas(directory):
    credits = read_grades(f"{directory}/credits.txt")
    overall_gpas = []

    with open(f"{directory}/overallGPAs.txt", 'w') as result_file:
        for course in ['math', 'chemistry', 'english']:
            scores = read_grades(f"{directory}/{course}.txt")
            points = convert_percentage_to_points(*scores)
            gpa = calculate_gpa(*points, *credits)
            overall_gpas.append(gpa)
            result_file.write(f"{course} GPA: {gpa:.2f}\n")

    return overall_gpas


class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self.overall_gpa = self.calculate_gpa()
        self.status = self.set_status()

    def calculate_gpa(self):
        points = [self.scores[course]['score'] for course in self.scores]
        credits = [self.scores[course]['credits'] for course in self.scores]
        return sum([point * credit for point, credit in zip(points, credits)]) / sum(credits)

    def set_status(self):
        return "Passed" if self.overall_gpa >= 1.0 else "Not Passed"

    def show_gpa(self):
        print(f"{self.name}'s GPA: {self.overall_gpa:.2f}")

    def show_status(self):
        print(f"{self.name}'s Status: {self.status}")

# Usage example
student_data = {'math': {'score': 4.3, 'credits': 4}, 'chemistry': {'score': 4.3, 'credits': 3},
                'english': {'score': 4.3, 'credits': 4}}
student = Student("Rakhmetuly Zhanserik", 3, student_data)
student.show_gpa()
student.show_status()
