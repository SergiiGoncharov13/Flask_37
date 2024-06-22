from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('/hello.html')

@app.route('/students')
def students():
    students = [
        ('Yaroslav', 'student'),
        ('Milan', 'student'),
        ('Maksym', 'student')
    ]
    return render_template('students.html', students=students)



if __name__ == '__main__':
    app.run(port=8080, debug=True)



