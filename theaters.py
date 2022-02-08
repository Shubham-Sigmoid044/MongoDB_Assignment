# Top 10 cities with the maximum number of theatres

t1 = collection4.aggregate([
  {"$group": {"_id": {"city": "$location.address.city"}, "numTheaters": {"$sum": 1}}},
  {"$sort": {"numTheaters": -1}},
  {"$limit": 10}
])

print(list(t1))



# ii. top 10 theatres nearby given coordinates

# extracted the theaterid and location in sepearte list

newTheater = collection4.aggregate([
    {
        "$project": {
            "_id": 0,
            "theaterId": 1,
            "location": {
                "type": "Point",
                "coordinates": "$location.geo.coordinates"
            },
            "address": {
                "street": "$location.address.street1",
                "city": "$location.address.city",
                "zipcode": "$location.address.zipcode"
            }
        }
    }
])

new_theater = list(newTheater)

coord = []
i_d = []

# print(new_theater)

# created a list of id and coordinates to update the theater so that I can easily create the 2dsphere index

for i in new_theater:
    t = [float(i['location']['coordinates'][0]['$numberDouble']), float(i['location']['coordinates'][1]['$numberDouble'])]
    coord.append(t)

    oid_str = i['theaterId']['$numberInt']
    i_d.append(oid_str)


# Updated all the values of theaters by adding coordinates in specific geospatial format so that index can be easily applied    

# for i in range(0, len(i_d)):
#     collection4.update_one({"theaterId.$numberInt": i_d[i]},
#                           {"$set": {"loc": {"type": "Point", "coordinates": [coord[i][0], coord[i][1]]}}})


# Created the index

# db.theaters.createIndex({"loc": "2dsphere"})

lat = float(input("Enter the latitude: "))
long = float(input("Enter the longitude: "))

# Searched for given lat and long values

nearby_theaters = collection4.find({
  "loc": {"$geoNear": {
    "$geometry": {
      "type": "Point",
      "coordinates": [
        lat,
        long
      ]
    },
    "$maxDistance": 50000,
    "$minDistance": 0
  }}
})

# -98.608055,
#         33.685692

for i in nearby_theaters:
    print(i)
