from forms import UserLoginForm
from models import User, Register, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, LoginManager, current_user, login_required 

auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

# auth2 = Blueprint('auth2', __name__, template_folder = 'auth_templates')

# api = Blueprint('api', __name__, url_prefix = '/api')

@auth.route('/signup', methods = ['GET', 'POST']) 
def signup():
    form = UserLoginForm() 

    try:
        if request.method == 'POST' and form.validate_on_submit(): 
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data 
            password = form.password.data 
            print(first_name, last_name, email, password)

            user = User(email, first_name, last_name,  password = password) 

            db.session.add(user)
            db.session.commit()

            flash(f'You have succesfully created a user account {email}', 'User-created')                                                                       
            return redirect(url_for('site.home'))        
    except:
        raise Exception('Invalid for data: Please check your form')
    return render_template('sign_up.html', form = form)


@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit(): 
            first_name = form.first_name.data
            last_name = form.last_name.data
            email = form.email.data
            password = form.password.data
            # print(email, password)

            logged_user = User.query.filter(User.email == email).first() 

            if logged_user and check_password_hash(logged_user.password, password):  
                login_user(logged_user) 
                flash('You have succesfully logged in. Please proceed. to building your car!', 'auth-success')
                return redirect(url_for('site.profile'))
            else:
                flash('You have failed in your attempt to access this content.', 'auth-failed')
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('sign_in.html', form = form)


@auth.route('/logout')
def logout():
    logout_user() 
    return redirect(url_for('site.home'))


