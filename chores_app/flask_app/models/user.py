from flask_app import app
from flask_app.models import chore, assigned_chore
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    schema_name = "chores_schema"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.is_parent = data['is_parent']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.chores = []

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("chores_schema").query_db(query, user)
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.", "registration")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.", "registration")
            is_valid = False
        if  user['is_parent'] == 'false':
            flash("You must have your parent or gaurdian register for this site first", "registration")
        if len(results) >= 1:
            flash("Email already taken.", "registration")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!", "registration")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", "registration")
            is_valid = False
        if user["password"] != user["confirm_password"]:
            flash("Passwords must match", "registration")
            is_valid = False
        return is_valid

    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, is_parent, email, password) VALUES (%(first_name)s, %(last_name)s, %(is_parent)s, %(email)s, %(password)s);"
        return connectToMySQL("chores_schema").query_db(query, data)

    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("chores_schema").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("chores_schema").query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users WHERE is_parent = 'False';"
        results = connectToMySQL('chores_schema').query_db(query)
        users = []
        for entry in results:
            users.append(cls(entry))
        return users

    @classmethod
    def get_user_by_chore_id(cls, data):
        query = "SELECT users.first_name FROM users JOIN assigned_chores ON assigned_chores.user_id = users.id JOIN chores ON assigned_chores.chore_id = chores.id WHERE chores.id = %(chore_id)s;"
        results = connectToMySQL("chores_schema").query_db(query, data)
        return cls(results[0])
