from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.sighting import Chore
from flask import render_template, redirect, request, session, flash

bcrypt = Bcrypt(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save_user(data)
    session['user_id'] = user_id
    return redirect("/family_dashboard90")

@app.route('/login', methods = ['POST'])
def login():
    user_in_db = User.get_user_by_email(request.form)
    if not user_in_db:
        flash("Invalid email/password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid email/password", "login")
        return redirect("/")
    session['user_id'] = user_in_db.id
    return redirect("/family_dashboard90")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/new_kid_form')
def new_kid_form(data):
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id'],
    }
    return render_template('new_chore.html', user = User.get_user_by_id(data))

@app.route('/register_kid', methods = ['POST'])
def register_kid():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save_user(data)
    return redirect("/family_dashboard90")
