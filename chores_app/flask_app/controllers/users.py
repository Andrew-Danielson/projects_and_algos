from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.models.user import User
from flask_app.models.chore import Chore
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
        "is_parent" : request.form['is_parent'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    userid = User.save_user(data)
    session['userid'] = userid
    return redirect("/family_dashboard")

@app.route('/login', methods = ['POST'])
def login():
    user_in_db = User.get_user_by_email(request.form)
    if not user_in_db:
        flash("Invalid email/password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid email/password", "login")
        return redirect("/")
    session['userid'] = user_in_db.id
    session['is_parent'] = user_in_db.is_parent
    return redirect("/family_dashboard")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/new_kid_form')
def new_kid_form():
    if "userid" not in session:
        return redirect('/logout')
    if session['is_parent'] == 'False':
        return redirect('/logout')
    data = {
        "id": session['userid'],
    }
    return render_template('new_kid_form.html', user = User.get_user_by_id(data))

@app.route('/register_kid', methods = ['POST'])
def register_kid():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "is_parent" : request.form['is_parent'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    userid = User.save_user(data)
    return redirect("/family_dashboard")
