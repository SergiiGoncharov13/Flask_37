from faker import Faker
from datetime import datetime

from models import db, Post
from app import app

fake = Faker()

NUM_RECORDS = 1

def add_fake_post():
    with app.app_context():
        for _ in range(NUM_RECORDS):
            title = fake.sentence(nb_words=6)
            content = fake.paragraph(nb_sentences=3)

            new_post = Post(title=title, content=content)
            db.session.add(new_post)
        
        db.session.commit()



if __name__ == '__main__':
    add_fake_post()



