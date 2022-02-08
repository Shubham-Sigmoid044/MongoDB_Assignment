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


    
    
    
    
    
# iii Given a year find the total number of comments created each month in that year

    
# converted object date type into date type

newMov = collection1.aggregate([
    {
        "$project": {
            "_id": 1,
            "date": 1
        }
    }
])

new_mov = list(newMov)

i_d = []
date_list = []

# use the list to hold the id and numberlong date format

for i in new_mov:
    oid_str = i['_id']
    oid2 = ObjectId(oid_str)
    i_d.append(oid2)
    date_list.append(bson.Int64(i['date']['$date']['$numberLong']))

# for i in range(0, len(i_d)):
#     print(i_d[i], date_list[i])

# Updated the comments with new dob format to make query easily

# for i in range(0, len(i_d)):
#     collection1.update_one({"_id": i_d[i]},
#                           {"$set": {"dob": date_list[i]}})




# converted numberlong format into date format to seperate month and year

# group by month to get the number of user each month

month_num_comments = collection1.aggregate([
  {
    "$project": {
      "_id": 0,
      "b_date": {"$convert": {"input": "$dob", "to": "date"}},
      "name": 1,
      "email": 1
    }
  },
  {
    "$project": {
      "name": 1,
      "email": 1,
      "b_date": 1,
      "year": {"$year": "$b_date"},
      "month": {"$month": "$b_date"}
    }
  },
  {
    "$match": {"year": 1998},
  },
  {"$group": {"_id": {"month": "$month"}, "numUser": {"$sum": 1}}}  
])

print(list(month_num_comments))

