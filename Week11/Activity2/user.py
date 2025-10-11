from db import db

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def user_register(self):
        db.users.insert_one({"username": self.username, "email": self.email})
        user_id = db.users.find_one({"username": self.username})["_id"]
        return user_id