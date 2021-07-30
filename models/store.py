import sqlite3
from db import db


class StoreModel(db.Model):
    # tell sqlalchemy which table to look for
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        # coz we are using lazy=dynamic, we can't use self.items directly use all method on that
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # the above code is doing the same
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cur.execute(query, (name,))
        # row = result.fetchone()
        #
        # if row:
        #     return cls(*row)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # query = "INSERT INTO items VALUES (?,?)"
        # cur.execute(query, (self.name, self.price))
        #
        # conn.commit()
        # conn.close()

    # def update(self):
    #     conn = sqlite3.connect('data.db')
    #     cur = conn.cursor()
    #
    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cur.execute(query, (self.price, self.name))
    #
    #     conn.commit()
    #     conn.close()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()