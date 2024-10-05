from flask import Flask, render_template, abort, request, make_response, redirect, url_for
import data


app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        title=data.title,
        subtitle=data.subtitle,
        description=data.description,
        departures=data.departures,
        tours=data.tours,
        cookie=request.cookies.get('username')
    )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not request.cookies.get('username') and request.method == 'POST':
        res = make_response('Setting a cookie')
        res.set_cookie('username', request.form.get('name'), max_age=60 * 60 * 24 * 365 * 2) 
        return res
    return render_template('login.html')

@app.route('/cookie')
def cookie():
    if not request.cookies.get('username') or request.cookies.get('username') == "None":
        return redirect(url_for('loggin'))
    else:
        res = make_response(f'Value of cookie foo is {request.cookies.get('username')}')
        return res

@app.route('/departures/<departure>/')
def departure_page(departure):
    tours = {tour_id: tour for tour_id, tour in data.tours.items() if tour['departure'] == departure}
    if not tours:
        abort(404)  # Return 404 if no tours found for the departure
    return render_template(
        'departure.html',
        title=data.title,
        departures=data.departures,
        departure=departure,
        tours=tours
    )

@app.route('/departures')
def departures_zero():
    return render_template('index.html')
 
@app.route('/tour/<int:tour_id>')
def tour_details(tour_id):
    tour = data.tours.get(tour_id)
    if not tour:
        abort(404)  # Return 404 if tour_id not found
    return render_template(
        'tour.html',
        title=data.title,
        departures=data.departures,
        tour=tour
    )


if __name__ == '__main__':
    app.run(debug=True)
