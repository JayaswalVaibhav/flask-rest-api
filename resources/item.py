import sqlite3
from flask_restful import Resource, reqparse
from flask import request
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'item': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with name {} already exists".format(name)}, 400

        data = request.get_json()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': "error occurred inserting an item"}, 500  # internal server error
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # query = "DELETE FROM items WHERE name=?"
        # cur.execute(query, (name,))
        #
        # conn.commit()
        # conn.close()
        return {'message': 'Item deleted'}

    def put(self, name):
        data = request.get_json()
        item = ItemModel.find_by_name(name)

        # updated_item = ItemModel(name, data['price'])
        if not item:
            item = ItemModel(name, data['price'], data['store_id'])
            # try:
            #     updated_item.insert()
            # except:
            #     return {'message': "error occurred inserting an item"}, 500
        else:
            item.price = data['price']
            # try:
            #     updated_item.update()
            # except:
            #     return {'message': "error occurred inserting an item"}, 500
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):

        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        #
        # query = "SELECT * FROM items"
        # result = cur.execute(query)
        #
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})
        #
        # conn.commit()
        # conn.close()

        return {'items': [item.json() for item in ItemModel.query.all()]}