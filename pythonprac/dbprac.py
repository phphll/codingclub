from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# doc = {'name':'c','age':17},
# doc = {'name':'d','age':18}
# db.users.insert_one(doc)

# same_ages = list(db.users.find({'age':18},{'_id':False}))
# # 전체를 찾을떄는 중괄호만 남겨둠
# for person in same_ages:
#     print(person)

# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user)

# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# db.users.update_many({'age':18},{'$set':{'age':19}})

# db.users.delete_one({'name':'bobby'})

# 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})

#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})

# quiz_1
# q_1 = db.movies.find_one({'title':'매트릭스'})
# print(q_1['point'])

# quiz_2
# q_2 = db.movies.find_one({'title':'매트릭스'})
# sam = q_2['point']
#
# movies = list(db.movies.find({'point':sam}))
#
# for q2 in movies:
#     print(q2['title'])

# quiz_3
# db.movies.update_one({'title':'매트릭스'},{'$set':{'point':0}})

# db.movies.delete_one({'age':0})

doc = {'rank':'18','title':'매트릭스','point':'0'}
db.movies.insert_one(doc)