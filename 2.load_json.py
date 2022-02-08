import pymongo
from pymongo import MongoClient
import re
import json
from bson import ObjectId

client = MongoClient('mongodb://127.0.0.1:27017/')

db = client["AssignmentData"]
collection1 = db.comments
collection2 = db.movies
collection3 = db.sessions
collection4 = db.theaters
collection5 = db.users
collection = db.test

coll_name = ["comments", "movies", "sessions", "theaters", "users"]

for i in coll_name:
    item_list = []
    with open(f'sample_mflix/{i}.json') as f:
        for json_obj in f:
            if json_obj:
                my_dict = json.loads(json_obj)
                my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
                item_list.append(my_dict)

    if i == "comments":
        collection1.insert_many(item_list)
    elif i == "movies":
        collection2.insert_many(item_list)
    elif i == "sessions":
        collection3.insert_many(item_list)
    elif i == "theaters":
        collection4.insert_many(item_list)
    else:
        collection5.insert_many(item_list)

# item_list = []
#
# with open('sample_mflix/users.json') as f:
#     for json_obj in f:
#         if json_obj:
#             my_dict = json.loads(json_obj)
#             my_dict["_id"] = ObjectId(my_dict["_id"]["$oid"])
#             item_list.append(my_dict)
#
# collection5.insert_many(item_list)
