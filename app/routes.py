from app import *
from flask import render_template, redirect, flash, request
from app.forms import *
from app.models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_required, login_user, logout_user

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/')
def home():
    return render_template('base.html')

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/add_following', methods = ['POST', 'GET'])
@login_required
def add_following():
    current_form = AddFollowingForm()
    user = User.query.all()

    if request.method == "POST":
        option = request.form.get('users')
        user_to_follow = User.query.filter_by(username = option).first()

        if user_to_follow:
            current_user.follow(user_to_follow)
            db.session.commit()
            return redirect('/homepage')
        else:
            flash("User doesn't exist")
            return redirect('/add_following')
       

    return render_template('add_following.html', form = current_form, user=user)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/create_account', methods = ['POST', 'GET'])
def create_account():
    current_form = CreateAccountForm()

    if current_form.validate_on_submit():

        username = User.query.filter_by(username = current_form.username.data).first()
        email = User.query.filter_by(email = current_form.email.data).first()

        if username:
            flash('Username is already taken!')
            return redirect('/create_account')
        if email:
            flash('Email is already in use!')
            return redirect('/create_account')

        new_user = User(email = current_form.email.data, username = current_form.username.data,
                        password = generate_password_hash(current_form.password.data))
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('create_account.html', form = current_form)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/create_post', methods = ['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category = 'error')
        else:
            post = Post(text = text, author = current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category = 'success')
            return redirect('/homepage')

    return render_template('create_post.html', user = current_user)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/delete/<int:id>')
@login_required
def delete_account(id):
    if id == current_user.id:
        db.session.delete(current_user)
        db.session.commit()
        return redirect('/create_account')
    else:
        return ("Sorry didn't work")

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/delete_post/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id = id).first()
    if post.author != current_user.id:
        return ("you dont have access")
    else:
        db.session.delete(post)
        db.session.commit()
        return redirect('/homepage')

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/homepage', methods = ['POST', 'GET'])
@login_required
def homepage():
    posts = Post.query.all()
    return render_template("homepage.html", username = current_user.username, posts = posts)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/login', methods = ['POST', 'GET'])
def login():
    current_form = LoginForm()

    if current_form.validate_on_submit():
        user = User.query.filter_by(username = current_form.username.data).first()

        if user is None or not user.check_password(current_form.password.data):
            flash('Invalid password!')
            return redirect('/login')

        login_user(user, remember = current_form.remember_me.data)
        return redirect('/homepage')

    return render_template('login.html', form = current_form)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged Out")
    return redirect('/login')

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/remove_following', methods = ['POST', 'GET'])
@login_required
def remove_following():
    current_form = RemoveFollowingForm()

    if current_form.validate_on_submit():
        user_to_remove_follow = User.query.filter_by(username = current_form.username.data).first()

        if user_to_remove_follow:
            current_user.unfollow(user_to_remove_follow)
            db.session.commit()
            return redirect('/homepage')
        else:
            flash('User does not exist')
            return redirect('/remove_following')

    return render_template('remove_following.html', form = current_form)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/update_password/<int:id>', methods=['GET', 'POST'])
@login_required
def update_password(id):
    form = UpdatePasswordForm()
    name_to_update = User.query.get_or_404(id)

    if request.method == "POST":
        name_to_update.password = request.form['password']
        name_to_update.password = generate_password_hash(name_to_update.password)
    
        db.session.commit()
        flash("Update Successful")
        return redirect('/login')

    return render_template("/update_password.html", form=form, name_to_update = name_to_update)

# -------------------------------------------------------------------------------------------------

'''
COMMENTS
 return render_template('login.html', name=name, a=a, form=current_form)
    - Renders the HTML file and returns it to the route, passing in the given variables
      which will then be interpreted by the {{ variable }} spots in the HTML file
'''
