# ii. Find top `N` directors -

# 1. who created the maximum number of movies

# group by directors and calculated numMovies for each

d1 = collection2.aggregate([
    {"$unwind": "$directors"},
    {"$group": {"_id": {"directors": "$directors"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": n}
])

# print(list(d1))


# 2. who created the maximum number of movies in a given year

year = input("Enter the year: ")

# group by given year to get the result

d2 = collection2.aggregate([
    {"$unwind": "$directors"},
    {"$match": {"year.$numberInt": "1994"}},
    {"$group": {"_id": {"directors": "$directors"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": n}
])

# print(list(d2))


# 3. who created the maximum number of movies for a given genre

d3 = collection2.aggregate([
    {"$unwind": "$directors"},
    {"$match": {"genres": "Drama"}},
    {"$group": {"_id": {"directors": "$directors"}, "numMovies": {"$sum": 1}}},
    {"$sort": {"numMovies": -1}},
    {"$limit": n}
])

# print((list(d3)))

