from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.chore import Chore
from flask import render_template, redirect, request, session, flash

@app.route('/family_dashboard')
def home():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
        }
    return render_template('/family_dashboard.html', user = User.get_user_by_id(data), all_chores = Chore.get_all_chores())

@app.route('/new_chore_form')
def new_form():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id'],
    }
    return render_template('new_chore.html', user = User.get_user_by_id(data))

@app.route('/create_chore', methods = ['POST'])
def create_chore():
    if not Chore.validate_chore(request.form):
        return redirect('/new_chore_form')
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
    }
    Chore.save_chore(data)
    return redirect('/family_dashboard')

@app.route('/chores/<int:user_id>')
def view_chores(user_id):
    if "user_id" not in session:
        return redirect('/logout')
    # chore_data = {
    #     'chore_id': chore_id
    # }
    data = {
        "id": session['user_id']
        }
    return render_template('chore.html', chore = Chore.get_chore_by_user_id(user_id), user = User.get_user_by_id(data))