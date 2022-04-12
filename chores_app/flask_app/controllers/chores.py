from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.chore import Chore
from flask_app.models.assigned_chore import Assigned_Chore
from flask import render_template, redirect, request, session, flash

@app.route('/family_dashboard')
def home():
    if "userid" not in session:
        return redirect('/logout')
    data = {
        "id": session['userid'],
        }
    return render_template('/family_dashboard.html', user = User.get_user_by_id(data), all_assigned_chores = Assigned_Chore.get_all_assigned_chores())

@app.route('/new_chore_form')
def new_form():
    if "userid" not in session:
        return redirect('/logout')
    if session['is_parent'] == 'False':
        return redirect('/logout')
    data = {
        "id": session['userid'],
    }
    return render_template('new_chore.html', user = User.get_user_by_id(data))

@app.route('/create_chore', methods = ['POST'])
def create_chore():
    if not Chore.validate_chore(request.form):
        return redirect('/new_chore_form')
    if "userid" not in session:
        return redirect('/logout')
    data = {
        "name" : request.form['name'],
        "description" : request.form['description'],
    }
    Chore.save_chore(data)
    return redirect('/family_dashboard')

@app.route('/chores/<int:id>')
def view_chores(id):
    if "userid" not in session:
        return redirect('/logout')
    data1 = {
        "user_id": session['userid']
        }
    data2 = {
        "id": session['userid']
        }
    return render_template('kid_dashboard.html', all_assigned_chores = Assigned_Chore.get_assigned_chore_by_user_id(data1), user = User.get_user_by_id(data2))

@app.route('/parent_dashboard')
def parent_home():
    if "userid" not in session:
        return redirect('/logout')
    if session['is_parent'] != 'True':
        return redirect('/family_dashboard')
    data = {
    "id": session['userid'],
    }
    return render_template('/parent_dashboard.html', sess_user = User.get_user_by_id(data), all_users = User.get_all_users(), all_chores = Chore.get_all_chores(), all_assigned_chores = Assigned_Chore.get_all_assigned_chores())

@app.route('/assign_chore', methods = ['POST'])
def assign_chore():
    if "userid" not in session:
        return redirect('/logout')
    if session['is_parent'] == 'False':
        return redirect('/logout')
    data = {
        "user_id" : request.form['user.id'],
        "chore_id" : request.form['chore.id'],
    }
    Assigned_Chore.assign_chore(data)
    return redirect('/family_dashboard')

@app.route('/finish_chore', methods = ['POST'])
def finish_chore():
    if "userid" not in session:
        return redirect('/logout')
    if session['is_parent'] == 'False':
        return redirect('/logout')
    print('HERE')
    data = {
        "id" : request.form['assigned_chore.id'],
    }
    print('HERE')
    print(data)
    print(type(data))
    Assigned_Chore.finish_chore(data)
    return redirect('/family_dashboard')