
# user_db = {"username1": "password123", "username2": "pass"}
user_db = {}

def user_register(username, password):
    if username in user_db:
        print("Цей логін вже використовується. Оберіть інший")
    else:
        user_db[username] = password
        print(f"Користувач {username} успішно зареєстрований")


def user_auth(username, password):
    if username not in user_db:
        print("Такого користувача не знайдено")
    else:
        if user_db[username] == password:
            print("Вхід у систему дозволено")
        else:
            print("Користувач увів невірний пароль")
        
    

if __name__ == "__main__":
    user_register("user1", "pass")
    user_auth("user1", "pass")      # -> вхід у систему дозволено
    user_auth("user1", "pass123")   # -> не вірно вказаний пароль
