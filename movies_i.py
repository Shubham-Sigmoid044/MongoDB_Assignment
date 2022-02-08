
# 1. with the highest IMDB rating

n = int(input("Enter the N: "))

# sorted with IMDB rating

m1 = collection2.find({}, {"_id": 1, "title": 1, "imdb.rating": 1}).sort("imdb.rating", -1).limit(n)

# print(list(m1))


# 2. with the highest IMDB rating in a given year

# matched with given year and sorted with IMDB rating

m2 = collection2.find({"year.$numberInt": "1916"}, {"_id": 0, "title": 1, "imdb.rating": 1, "year": 1}) \
    .sort("imdb.rating", -1).limit(n)

# print(list(m2))


# 3. with highest IMDB rating with number of votes > 1000

# searched only those values whose imdb is greater than 1000

m3 = collection2.find({"imdb.votes.$numberInt": {"$gt": "1000"}},
                      {"_id": 0, "title": 1, "imdb.votes": 1, "imdb.rating": 1}).sort("imdb.rating", -1).limit(n)

# print(list(m3))


# 4. with title matching a given pattern sorted by highest tomatoes ratings

# searched the title only matching with given regex

pattern = input("Enter the pattern: ")
# pattern = "little"

m4 = collection2.find({"title": {"$regex": pattern}}, {"_id": 0, "title": 1, "tomatoes.viewer.rating": 1}) \
    .sort("tomatoes.viewer.rating", -1)

# print(list(m4))
