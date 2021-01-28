from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# target_movie = db.movies.find_one({'title':'매트릭스'})
# print(target_movie['star'])
#
# target_star = target_movie['star']
# movies = list(db.movies.find({'star':target_star}))
#
# for movie in movies:
#     print(movie['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})