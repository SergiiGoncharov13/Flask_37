from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('/index.html')

def grade_value(grade):
    grade_mapping = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    return grade_mapping.get(grade, 0)


@app.route('/students')
def students():
    all_students = [
        ('Yaroslav', 'A'),
        ('Milan', 'B'),
        ('Maksym', 'A')
    ]

    all_students_dict = [{'name': name, 'grade': grade} for name, grade in all_students]
    grade = request.args.get('grade')
    sort_by = request.args.get('sort')

    students = all_students_dict
    if grade:
        students = [student for student in all_students if student['grade'] == grade]

    if sort_by:
        students = sorted(students, key=lambda x: x[sort_by])

    # Find the best student based on the highest grade value
    best_student = max(students, key=lambda x: grade_value(x['grade']), default=None)
    
    return render_template('students.html', students=students, best_student=best_student)



if __name__ == '__main__':
    app.run(port=8080, debug=True)



