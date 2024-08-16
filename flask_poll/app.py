from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)
poll_data = {
    'question': 'Which web framework do you use?',
    'fields': ['Flask', 'Django', 'FastAPI']
}
filename = 'data.txt'

@app.route('/')
def index():
    return render_template('poll.html', data=poll_data)


@app.route('/poll')
def poll():
    vote = request.args.get('field')
    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()
    return redirect(url_for('results'))


@app.route('/results')
def results():
    with open(filename, 'r') as file:
        votes = {choise: 0 for choise in poll_data['fields']}
        for line in file:
            vote = line.rstrip('\n')
            votes[vote] += 1

    total_votes = sum(votes.values())
    return render_template('results.html', data=poll_data, votes=votes, total_votes=total_votes)



if __name__ == '__main__':
    app.run(debug=True)