
# # user_db = {"username1": "password123", "username2": "pass"}
# user_db = {}

# def user_register(username, password):
#     if username in user_db:
#         print("Цей логін вже використовується. Оберіть інший")
#     else:
#         user_db[username] = password
#         print(f"Користувач {username} успішно зареєстрований")


# def user_auth(username, password):
#     if username not in user_db:
#         print("Такого користувача не знайдено")
#     else:
#         if user_db[username] == password:
#             print("Вхід у систему дозволено")
#         else:
#             print("Користувач увів невірний пароль")
        
    

# if __name__ == "__main__":
#     user_register("user1", "pass")
#     user_auth("user1", "pass")      # -> вхід у систему дозволено
#     user_auth("user1", "pass123")   # -> не вірно вказаний пароль



# написати ф-ю user_auth яка буде перевіряти логін і пароль і вразі успіху - пускати в систему
# написать 2 тести. логін і пароль вірний. логін вірний і пароль не вірний

# користувач починає реєструватись
# email@example.com
# password12

# password12 -> action -> hash_password ("dasbvfyi2gw38rg8327grfd8ywegf87egw87ge8wgf87eg7g2w3789gr8g")

# email@example.com
# dasbvfyi2gw38rg8327grfd8ywegf87egw87ge8wgf87eg7g2w3789gr8g

# password -> hash_password
# 123456 -> hash_password12

# 8 A a 1 .

# 4wbnf9u4brf723gb78fdg723g79fg9wfdsdf

import hashlib


user_db = {}


def create_hash_password(password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password

def user_register(username, password):
    if username in user_db:
        print("Цей логін вже використовується. Оберіть інший")
    else:
        user_db[username] = create_hash_password(password)
        print(f"Користувач {username} успішно зареєстрований")


def user_auth(username, password):
    if username not in user_db:
        print("Такого користувача не знайдено")
    else:
        if user_db[username] == create_hash_password(password):
            print("Вхід у систему дозволено")
        else:
            print("Користувач увів невірний пароль")
        
    

if __name__ == "__main__":
    user_register("user1", "pass")
    user_auth("user1", "pass")      # -> вхід у систему дозволено
    user_auth("user1", "pass123")   # -> не вірно вказаний пароль

    print(user_db)
