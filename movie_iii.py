# iii. Find top `N` actors - 

# 1. who starred in the maximum number of movies

# as cast is given in form of array, unwind all the cast and the group by the cast to get the results

h1 = collection2.aggregate([
    {"$unwind": "$cast"},
    {"$group": {"_id": {"actor": "$cast"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": n}
])

# print((list(h1)))


# 2. who starred in the maximum number of movies in a given year

# unwind the cast and match with given year and then group by actors

h2 = collection2.aggregate([
    {"$unwind": "$cast"},
    {"$match": {"year.$numberInt": "1998"}},
    {"$group": {"_id": {"actor": "$cast"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": n}
])

# print(list(h2))



# 3. who starred in the maximum number of movies for a given genre

# unwind the cast and match with given genre and then group by actors

h3 = collection2.aggregate([
    {"$unwind": "$cast"},
    {"$match": {"genres": "Drama"}},
    {"$group": {"_id": {"actors": "$cast"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": n}
])

# print(list(h3))
