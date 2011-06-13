import datetime
from pymongo import Connection
from bson import ObjectId
from settings import MONGO_HOST, MONGO_PORT


connection = Connection(MONGO_HOST, MONGO_PORT)
db = connection.eatracker


def read_eatings():
    return db.eating.find()


def create_eating(data):
    item = {'type': data.get('type'),
            'dishes': data.getlist('dishes')}
    if 'comment' in data:
        item.update(comment=data.get('comment'))
    if 'date' in data:
        item.update(date=data.get('date'))
    else:
        item.update(date=datetime.datetime.utcnow())
    return db.eating.insert(item)


def update_eating(data, id):
    item = db.eating.find_one({'_id': ObjectId(id)})
    if 'type' in data:
        item.update(type=data.get('type'))
    if 'comment' in data:
        item.update(comment=data.get('comment'))
    if 'date' in data:
        item.update(date=data.get('date'))
    if 'dishes' in data:
        item.update(dishes=data.getlist('dishes'))
    return db.eating.save(item)


def remove_eating(id):
    db.eating.remove({'_id': ObjectId(id)})
