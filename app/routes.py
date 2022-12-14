from app import *
from flask import render_template, redirect, flash, request, Response
from app.forms import *
from app.models import *
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_required, login_user, logout_user

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/') # base route
def home():
    return render_template('base.html')

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/add_following', methods = ['POST', 'GET']) # allows user to follow someone
@login_required
def add_following():
    current_form = AddFollowingForm() # initializes add following form
    user = User.query.all() # lets us display all users in the database and pass it to the template

    if request.method == "POST":
        option = request.form.get('users')
        user_to_follow = User.query.filter_by(username = option).first() # tries to find user that they wanted to follow in database

        if user_to_follow: #  validates if user is found to follow
            current_user.follow(user_to_follow) # follows user and commits to database
            db.session.commit()
            return redirect('/homepage')
        else: # gives error is user is not found
            flash("User doesn't exist") 
            return redirect('/add_following')   


    return render_template('add_following.html', form = current_form, user = user)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/create_account', methods = ['POST', 'GET']) # allows user to create an account
def create_account():
    current_form = CreateAccountForm() # initializes form for creating account

    if current_form.validate_on_submit(): # checks input to see if form is filled out

        username = User.query.filter_by(username = current_form.username.data).first() # searches for username and email in database to check prior existence
        email = User.query.filter_by(email = current_form.email.data).first()

        if username: # gives an error and redirects if username or email is un-usable
            flash('Username is already taken!')
            return redirect('/create_account')
        if email:
            flash('Email is already in use!')
            return redirect('/create_account')

        new_user = User(email = current_form.email.data, username = current_form.username.data, # creates new user with given info
                        password = generate_password_hash(current_form.password.data)) # generates password hash to store password safely

        db.session.add(new_user) # adds new user to database and logs in
        db.session.commit()
        login_user(new_user)
        current_user.follow(current_user) # has user follow itself automatically when they make an account as a way to see their own posts in the feed
        db.session.commit()
        return redirect('/homepage')

    return render_template('create_account.html', form = current_form)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/create_post', methods = ['GET', 'POST']) # allows user to create post
@login_required
def create_post():
    if request.method == "POST": # retriving text from text box when submit is hit
        file = request.files['posted']
        text = request.form.get('text')
        
        if text == ' ':
            flash('Post cannot be empty', category = 'error')
        
        elif file: # when there is a file present will pass through this
            post_with_image = Post(text = text, author_id = current_user.id, author_str = current_user.username, image_name = file.filename, image = file.read())
            db.session.add(post_with_image)
            db.session.commit()
            flash('Post created!', category = 'success')
            return redirect('/homepage')

        else: # this is if post is empty
            post = Post(text = text, author_id = current_user.id, author_str = current_user.username, image_name = None, image = None)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category = 'success')
            return redirect('/homepage')

    return render_template('create_post.html', user = current_user)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/delete/<int:id>') # deletes current account
@login_required
def delete_account(id):
    if id == current_user.id: # compares against current user
        db.session.delete(current_user)
        db.session.commit()
        return redirect('/create_account')
    else:
        return ("Sorry didn't work")

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/delete_post/<int:id>') # allows user to delete post
@login_required
def delete_post(id):
    post = Post.query.filter_by(id = id).first() # queries the values according to an id that matches the database
    if post.author_id != current_user.id: # validates that the user is not deleting someone else's post
        flash('Cannot delete this post')
        return redirect('/homepage')
    else:
        db.session.delete(post) # deletes post from database
        db.session.commit()
        return redirect('/homepage')

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/homepage', methods = ['POST', 'GET']) # user homepage
@login_required
def homepage():
    posts = current_user.followed_posts() # grabs all the posts from the current users followers
    return render_template("homepage.html", username = current_user.username, posts = posts)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/login', methods = ['POST', 'GET']) # allows user to login
def login():
    current_form = LoginForm() # initializes form for login

    if current_form.validate_on_submit():
        user = User.query.filter_by(username = current_form.username.data).first() # sees if the username given exists in the database

        if user is None or not user.check_password(current_form.password.data): # checks if the user logged in with the proper password
            flash('Invalid password!')
            return redirect('/login')

        login_user(user, remember = current_form.remember_me.data) # logs in user
        return redirect('/homepage')

    return render_template('login.html', form = current_form)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/logout') # allows user to logout
@login_required
def logout():
    logout_user() # logs out user
    flash("Logged Out")
    return redirect('/login')

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/remove_following', methods = ['POST', 'GET']) # allows user to stop following someone
@login_required
def remove_following():
    current_form = RemoveFollowingForm() # initializes form to remove follower
    user = User.query.all()
    
    if request.method == "POST": # validates that the request method is a POST before looking for given user
        option = request.form.get('users')
        user_to_remove_follow = User.query.filter_by(username = option).first() # tries to find user to remove from follower list

        if user_to_remove_follow: # validates if the user was found
            current_user.unfollow(user_to_remove_follow) # removes user from follow list
            db.session.commit()
            return redirect('/homepage')
        else: # gives error if user didn't exist
            flash("User doesn't exist")
            return redirect('/remove_following')

    return render_template('remove_following.html', form = current_form, user = user)

# -------------------------------------------------------------------------------------------------

@myapp_obj.route('/update_password/<int:id>', methods = ['GET', 'POST']) # allows user to update password
@login_required
def update_password(id):
    form = UpdatePasswordForm() # initializes form for updating password
    name_to_update = User.query.get_or_404(id) # queries name to update to be used later

    if request.method == "POST": # verifies POST request
        name_to_update.password = request.form['password'] # updates password with new password after its hashed
        name_to_update.password = generate_password_hash(name_to_update.password)
    
        db.session.commit()
        flash("Update Successful")
        return redirect('/login')

    return render_template("/update_password.html", form = form, name_to_update = name_to_update)

# -------------------------------------------------------------------------------------------------
@myapp_obj.route('/get_image/<int:id>') # gets the images shown on homepage to display
@login_required
def get_image(id):
    img = Post.query.filter_by(id = id).first() # uses the post id to find the right image to display

    return Response(img.image, content_type = img)
# -------------------------------------------------------------------------------------------------