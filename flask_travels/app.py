from flask import Flask, render_template
import data


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', 
        departures=data.departures,
        title=data.title,
        subtitle=data.subtitle,
        description=data.description,
        tours=data.tours
        )


@app.route('/departures/<departure>')
def departure(departure):
    tours = dict(filter(lambda tour: tour[1]['departure'] == departure, data.tours.items()))
    if tours:
        return render_template('departure.html',
                departure=departure,
                title=data.title,
                departures=data.departures,
                tours=data.tours)
    else:
        abort(404)

@app.route('/departures')
def departures_zero():
    return render_template('index.html')

    
@app.route('/tours/<int:id>')
def list_tours(id):
    return render_template('tour.html',
        tour=data.tours[id],
        title=data.title,
        departures=data.departures)



if __name__ == '__main__':
    app.run(debug=True)
