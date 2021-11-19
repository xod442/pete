from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')

mydb = client["app_db"]
known = mydb["user"]

l1={"name":"rick", "age":61}
l2={"name":"bob", "age":21}
l3={"name":"joe", "age":41}
list_o_things = [l1,l2,l3]
print(list_o_things)
new_record = {}

for n in list_o_things:
    print(n['name'])
    if known.count_documents({"name": n['name']}) == 0:
        print('skippy')
        new_record['name'] = n['name']
        new_record['age'] = n['age']
        write_record = known.insert_one(new_record)
        new_record={}

    else:
        records='Fail to write mongo record, possible duplicate'
