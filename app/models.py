from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin
from datetime import datetime

followers = db.Table('followers', # creates follower table template with relationship for follower/following
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model, UserMixin): # creates user model with info such as id, username, password, email, posts, and followed
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(32), unique = True)
    posts = db.relationship('Post', backref='user', passive_deletes=True)
    followed = db.relationship('User', 
        secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic'
    )

    def follow(self, user): # follow function
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user): # follow function
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user): # checks if following
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
    
    def set_password(self, password): # function to set password
        self.password = generate_password_hash(password)

    def check_password(self, password): # function to check password
        return check_password_hash(self.password, password)
    
    def followed_posts(self): # queries, sorts, and joins  all of the followed users' posts ordered by the timestamp
        return Post.query.join(followers, (followers.c.followed_id == Post.author_id)).filter(
            followers.c.follower_id == self.id).order_by(Post.timestamp.desc())

    def __repr__(self):
        return f'<User {self.username}>'

class Post(db.Model): # posts model to store all posts with images, and link them to the appropriate user ID
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    image_name = db.Column(db.String(50))
    image = db.Column(db.LargeBinary)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = "CASCADE"), nullable = False)
    author_str = db.Column(db.String)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)

@login.user_loader
def load_user(id): # function to load a user
    return User.query.get(int(id))