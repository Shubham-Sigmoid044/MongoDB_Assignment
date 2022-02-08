# 1. Find top 10 users who made the maximum number of comments


# Group by email as email of user is unique to get number of users for comments
max_user = collection1.aggregate([
    {"$group": {"_id": {"email": "$email"}, "numUsers": {"$sum": 1}}},
    {"$sort": {"numUsers": -1}},
    {"$limit": 10}
])

# print(list(max_user))


# 2. Find top 10 movies with most comments

# Got each individual movie_id with number of comments on each movie_id

movie_with_comments = collection1.aggregate([
    {"$group": {"_id": {"movie_id": "$movie_id"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": 10}
])

# To print the name of each movie created a list of each id

movId = (list(movie_with_comments))

mov_id = []

# Converted bson objectId to convert in appropriate format and used to find all Ids in movie

for i in range(0, len(movId)):
    oid_str = movId[i]['_id']['movie_id']['$oid']
    oid2 = ObjectId(oid_str)
    mov_id.append(oid2)

# print(mov_id)

for id1 in mov_id:
    val = collection2.find({"_id": id1}, {"_id": 0, "title": 1, })
    print(list(val))


