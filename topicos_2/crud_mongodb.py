from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://aluno:aluno@cluster0.e24zln7.mongodb.net/?retryWrites=true&w=majority")
db = client["jonasdb"]
collection = db["produtodb"]

# Função para criar um usuário
def insert(data):
    result = collection.insert_one(data)
    return str(result.inserted_id)

# Função para obter todos os usuários
def get_all_produtodb():
    produtodb = collection.find()
    return [user for user in produtodb]

# Função para obter um usuário pelo ID
def get_user_by_id(_id):
    user = collection.find_one({"_id": ObjectId(_id)})
    return user

# Função para atualizar um usuário pelo ID
def update_user(_id, new_data):
    result = collection.update_one({"_id": ObjectId(_id)}, {"$set": new_data})
    return result.modified_count

# Função para excluir um usuário pelo ID
def delete_user(_id):
    result = collection.delete_one({"_id": ObjectId(_id)})
    return result.deleted_count

if __name__ == "__main__":

    data = {"nome" : "Maçã",
                 "validade" : "02/12/2023",
                 "quantidade" : 3}

    # Create
    created__id = insert(data)

    # Read all
    all_produtodb = get_all_produtodb()
    print("Produtos:")
    for user in all_produtodb:
        print(user)

   

    # Update
    _id_to_update = created__id
    update_data = {"quantidade" : 6}
    updated_count = update_user(_id_to_update, update_data)

    # Read all after update
    all_produtodb_after_update = get_all_produtodb()
    print("Produtos depois do UPDATE:")
    for user in all_produtodb_after_update:
        print(user)

    # Delete
    _id_delete = created__id
    deleted_count = delete_user(_id_delete)

    # Read all after delete
    all_produtodb_after_delete = get_all_produtodb()
    print("Produtos depois do DELETE:")
    for user in all_produtodb_after_delete:
        print(user)


pip install pymongo

python crud_mongodb.py