# Top 10 cities with the maximum number of theatres

t1 = collection4.aggregate([
  {"$group": {"_id": {"city": "$location.address.city"}, "numTheaters": {"$sum": 1}}},
  {"$sort": {"numTheaters": -1}},
  {"$limit": 10}
])

print(list(t1))
