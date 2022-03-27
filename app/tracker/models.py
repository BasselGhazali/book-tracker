from app import db
from datetime import datetime


class Publication(db.Model):
    __tablename__ = 'publication'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Publisher ID {}, {}'.format(self.id, self.name)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(500))
    image = db.Column(db.String(100))
    tags = db.Column(db.String(1000))  # TODO replace string with Enum
    price = db.Column(db.Float)
    vendors = db.Column(db.String(1000))  # TODO replace string with Enum
    genre = db.Column(db.String(1000))  # TODO replace string with Enum
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
    date_added = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, title, author, image, tags, price, vendors, genre, pub_id):
        self.title = title
        self.author = author
        self.image = image
        self.tags = tags
        self.price = price
        self.vendors = vendors
        self.genre = genre
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)
