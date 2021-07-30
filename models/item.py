import sqlite3
from db import db


class ItemModel(db.Model):
    # tell sqlalchemy which table to look for
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # store_id
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

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