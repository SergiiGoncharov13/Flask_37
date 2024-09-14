from flask import Flask, request, render_template
import flask_wtf
import wtforms


class SubscriptionForm(flask_wtf.FlaskForm):
    name = wtforms.StringField('Name')
    email = wtforms.StringField('Email')
    submit = wtforms.SubmitField('Submit')


class IcecreamForm(flask_wtf.FlaskForm):
    tastes = wtforms.SelectField('Tasty')
    topping = wtforms.SelectMultipleField('Topping')
    cup_size = wtforms.RadioField('Cup')
    submit = wtforms.SubmitField('Submit')


class RegistrationForm(flask_wtf.FlaskForm):
    email = wtforms.StringField('Email')
    password = wtforms.PasswordField('Password')
    submit = wtforms.SubmitField('Submit')
    remember = wtforms.BooleanField('Remember me')


def is_luggage_weight_valid(form, field):
    if field.data > 30 or field.data < 0:
        raise wtforms.validators.ValidationError('incorrect weight')


class LuggageForm(flask_wtf.FlaskForm):
    surname = wtforms.StringField('Surname', validators=[wtforms.validators.InputRequired()])
    name = wtforms.StringField('Name', validators=[wtforms.validators.InputRequired()])
    pass_id = wtforms.IntegerField('ID number', validators=[wtforms.validators.InputRequired()])
    luggage_weight = wtforms.IntegerField('Weight', validators=[wtforms.validators.InputRequired(), is_luggage_weight_valid])
    submit = wtforms.SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def index():
    return 'Flask WTF form. Home page'


@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    form = SubscriptionForm()
    if request.method == 'GET':
        return render_template('subscribe.html', form=form)
    return form.name.data


@app.route('/ice', methods=['GET', 'POST'])
def ice():
    form = IcecreamForm()
    form.tastes.choices = [('vanila', 'vanila'), ('choko', 'choko'), ('mango', 'mango')]
    form.topping.choices = [('coffee', 'coffee'), ('strawberry', 'strawberry')]
    form.cup_size.choices = [('little', 'little'), ('medium', 'medium'), ('big', 'big')]
    if request.method == 'GET':
        return render_template('ice.html', form=form)
    return form.tastes.data


@app.route('/register', methods=['GET', 'POST'])
def sign():
    form = RegistrationForm()
    if request.method == 'GET':
        return render_template('sign.html', form=form)
    return form.email.data


@app.route('/luggage', methods=['GET', 'POST'])
def luggage():
    form = LuggageForm()
    if request.method == 'GET':
        return render_template('luggage.html', form=form)
    if form.validate_on_submit():
        return 'ok'
    else:
        return f'{form.errors}'


if __name__ == '__main__':
    app.run(debug=True)