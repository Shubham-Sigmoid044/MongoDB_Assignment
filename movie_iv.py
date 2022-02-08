# iv Find top `N` movies for each genre with the highest IMDB rating

# unwind the genre and added all the genre to distGenres using $addToSet to include only distinct genre value using group by

genres = collection2.aggregate([
    {"$unwind": "$genres"},
    {"$group": {"_id": None, "distGenres": {"$addToSet": "$genres"}}},
    {"$project": {"_id": 0}}
])

y = list(genres)
all_genres = y[0]['distGenres']
# print(all_genres)

# Used this list of genre to find all N movies sorted by imdb rating

for i in all_genres:
    print(f"Highest IMDB rated movies for {i} Genre is: ")
    mov = collection2.find({"genres": i}, {"_id": 0, "title": 1, "imdb.rating": 1}).sort("imdb.rating", -1).limit(n)
    for j in mov:
        print(j)
