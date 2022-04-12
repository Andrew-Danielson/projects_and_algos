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

    @classmethod
    def get_all_chores(cls):
        query = "SELECT * FROM chores;"
        results = connectToMySQL('chores_schema').query_db(query)
        chores = []
        for entry in results:
            chores.append(cls(entry))
        return chores

    @classmethod
    def save_chore(cls, data):
        pass
        query = "INSERT INTO chores (name, description) VALUES (%(name)s, %(description)s);"
        return connectToMySQL("chores_schema").query_db(query, data)

    # @classmethod
    # def get_chore_by_user_id(cls, data):
    #     query = "SELECT * FROM chores JOIN assigned_chores ON assigned_chores.chore_id = chores.id JOIN users ON assigned_chores.user_id = users.id WHERE users.id =  %(user_id)s;"
    #     results = connectToMySQL("chores_schema").query_db(query, data)
    #     return cls(results[0])