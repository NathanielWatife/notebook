from flask import Blueprint, render_template, flash, request

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 5:
            flash("email is too short.", category='error')
        elif len(first_name) < 3:
            flash("Name too short", category='error')
        elif password1 != password2:
            flash('Password don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password too short', category='error')
        else:
            flash('Accoun created', category='success') 
    return render_template('signup.html')
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
@auth.route('/logout')
def logout():
    return render_template('logout.html') 