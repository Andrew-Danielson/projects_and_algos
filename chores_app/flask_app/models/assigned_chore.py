# from flask_app.controllers.chores import assign_chore
from flask_app import app
from flask_app.models import user
from flask_app.models import chore
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Assigned_Chore:
    schema_name = "chores_schema"

    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.chore_id = data['chore_id']
        self.is_finished = data['is_finished']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.chore = []

    @classmethod
    def get_all_assigned_chores(cls):
        query = "SELECT * FROM assigned_chores JOIN chores ON assigned_chores.chore_id = chores.id JOIN users ON assigned_chores.user_id = users.id"
        results = connectToMySQL("chores_schema").query_db(query)
        chores = []
        for row in results:
            chore_instance = cls(row)
            user_data = {
                "user_id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'], 
                "is_parent" : row['is_parent'],
                "id" : row["id"],
                "is_finished" :row['is_finished'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
                "chore_id" : row['chores.id'],
                "name" : row['name'],
                "description" : row['description'], 
            }
            chores.append(user_data)
            print(chores)
        return chores

    @classmethod
    def get_assigned_chore_by_user_id(cls, data):
        query = "SELECT * FROM assigned_chores JOIN chores ON assigned_chores.chore_id = chores.id JOIN users ON assigned_chores.user_id = users.id WHERE users.id = %(user_id)s AND assigned_chores.is_finished = 'False';"
        results = connectToMySQL("chores_schema").query_db(query, data)
        print('HERE')
        print(type(results))
        print(type(results[0]))
        print(results)
        chores = []
        for row in results:
            chore_instance = cls(row)
            print(chore_instance.id)
            print(chore_instance.is_finished)
            user_data = {
                "user_id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'], 
                "is_parent" : row['is_parent'],
                "id" : row["id"],
                "is_finished" :row['is_finished'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at'],
                "chore_id" : row['chores.id'],
                "name" : row['name'],
                "description" : row['description'], 
            }
            chores.append(user_data)
            print(chores)
        return chores

    @classmethod
    def assign_chore(cls, data):
        query = "INSERT INTO assigned_chores (user_id, chore_id) VALUES (%(user_id)s, %(chore_id)s);"
        return connectToMySQL("chores_schema").query_db(query, data)

    @classmethod
    def finish_chore(cls, data):
        query = "UPDATE assigned_chores SET is_finished = 'true' WHERE assigned_chores.id = %(id)s;"
        return connectToMySQL("chores_schema").query_db(query, data)