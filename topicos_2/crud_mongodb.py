from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://aluno:aluno@cluster0.e24zln7.mongodb.net/?retryWrites=true&w=majority")
db = client["jonasdb"]
collection = db["produtodb"]

def insert(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

def get_all_produtodb():
    produtodb = collection.find()
    return [user for user in produtodb]

def get_user_by_id(_id):
    user = collection.find_one({"_id": ObjectId(_id)})
    return user

def update_user(_id, new_data):
    result = collection.update_one({"_id": ObjectId(_id)}, {"$set": new_data})
    return result.modified_count

def delete_user(_id):
    result = collection.delete_one({"_id": ObjectId(_id)})
    return result.deleted_count

if __name__ == "__main__":

    data = {"nome" : "Maçã",
                 "validade" : "02/12/2023",
                 "quantidade" : 3}

    created__id = insert(data)

    all_produtodb = get_all_produtodb()
    print("Produtos:")
    for user in all_produtodb:
        print(user)

    # Update
    _id_to_update = created__id
    update_data = {"quantidade" : 6}
    updated_count = update_user(_id_to_update, update_data)

    all_produtodb_after_update = get_all_produtodb()
    print("Produtos depois do UPDATE:")
    for user in all_produtodb_after_update:
        print(user)

    
    # Delete
    _id_delete = created__id
    deleted_count = delete_user(_id_delete)

    all_produtodb_after_delete = get_all_produtodb()
    print("Produtos depois do DELETE:")
    for user in all_produtodb_after_delete:
        print(user)


pip install pymongo==3.7.2
pip install dnspython

python crud_mongodb.py
