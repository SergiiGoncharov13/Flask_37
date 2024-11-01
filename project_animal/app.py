from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# db model
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    habitat = db.Column(db.String(100), nullable=False)
    diet = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)


# # create db
# with app.app_context():
#     db.create_all()


@app.route('/')
def index():
    animals = Animal.query.all()
    return render_template('index.html', animals=animals)


@app.route('/add', methods=['GET', 'POST'])
def add_animal():
    if request.method == 'POST':
        name = request.form['name']
        habitat = request.form['habitat']
        diet = request.form['diet']
        description = request.form['description']
        new_animal = Animal(name=name, habitat=habitat, diet=diet, description=description)
        db.session.add(new_animal)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_animal.html')


@app.route('/animal/<int:id>')
def animal_detail(id):
    animal = Animal.query.get_or_404(id)
    return render_template('animal_detail.html', animal=animal)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)