from flask_app import app
from flask_app.models import user
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Chore:
    schema_name = "chores_schema"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.is_finished = data['is_finished']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @staticmethod
    def validate_chore(chore):
        is_valid = True
        query = "SELECT * FROM chores WHERE chores.id = %(chore_id)s"
        results = connectToMySQL("chores_schema").query_db(query, chore)
        if len(chore['name']) < 2:
            flash("The name of the chore must be at least 2 characters", "chore")
            is_valid = False
        if len(chore['description']) < 2:
            flash("The description of the chore must be at least 2 characters", "chore")
            is_valid = False
        return is_valid

    @staticmethod
    def save_chore(cls, data):
        pass
        query = "INSERT INTO chores (name, description) VALUES (%(name)s, %(description)s);"
        return connectToMySQL("chores_schema").query_db(query, data)

    @staticmethod
    def get_all_chores(cls):
        query = "SELECT * FROM chores JOIN assigned_chores ON assigned_chores.chore_id = chores.id JOIN users ON assigned_chores.user_id = users.id"
        results = connectToMySQL("chores_schema").query_db(query)
        chores = []
        for row in results:
            chore_instance = cls(row)
            user_data = {
                "id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'], 
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['users.created_at'],
                "updated_at" : row['users.updated_at']
            }
            this_user = user.User(user_data)
            chore_instance.user = this_user
            chores.append(chore_instance)
        return chores

    @staticmethod
    def assign_chore(cls, data):
        query = "INSERT INTO assigned_chores (user_id, chored_id) VALUES (%(user_id)s, %(chore_id)s);"
        return connectToMySQL("chores_schema").query_db(query, data)

    @staticmethod
    def finish_chore(cls, data):
        query = "UPDATE assigned_chores SET is_finished = 'True' WHERE assigned_chores.id = %(assigned_chore_id)s"
        return connectToMySQL("chores_schema").query_db(query, data)

    @staticmethod
    def get_chore_by_chore_id(cls, data):
        query = "SELECT * FROM chores JOIN assigned_chores ON assigned_chores.chore_id = chores.id JOIN users ON assigned_chores.user_id = users.id WHERE chores.id = %(chore_id)s;"
        results = connectToMySQL("chores_schema").query_db(query, data)
        chore = cls(results[0])
        user_data = {
            "id" : results[0]['users.id'],
            "first_name" : results[0]['first_name'],
            "last_name" : results[0]['last_name'],
            "age" : results[0]['age'],
            "email" : results[0]['email'],
            "password" : results[0]['password'],
            "created_at" : results[0]['users.created_at'],
            "updated_at" : results[0]['users.updated_at']
            }
        this_user = user.User(user_data)
        chore.user = this_user
        return chore


    @staticmethod
    def get_chore_by_user_id(cls, data):
        query = "SELECT * FROM chores JOIN assigned_chores ON assigned_chores.chore_id = chores.id JOIN users ON assigned_chores.user_id = users.id WHERE users.id =  %(user_id)s;"
        results = connectToMySQL("chores_schema").query_db(query, data)
        return cls(results[0])