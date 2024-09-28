from flask import Flask, render_template, request, redirect, url_for


from models import db, Post
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['POST'])
def add_post():
    title = request.form.get('title')
    content = request.form.get('content')

    if title and content:
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
    
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

