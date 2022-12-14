# IRL Patch
- Alexander Pereira (@50xp50)
- Shubham Mishra (@shubhammishra-2020) - Team Lead
- Henry Choy (@hfcphoenix)
- Marcus Lang (@MarcoPolo987)

# About
This project is about practicing and utilizing the different libraries
and methods that we have learned throughout the semester. We had to work
together in a team environment, and build a twitter clone website. This
website took the use of flask for building the bulk of the website,
SQLAlchemy for setting up and managing the database, and other smaller
libaries for things such as forms and CAPTCHAS.

# Functional Requirements Implemented
1. Login = Alexander
2. Logout sceen = Alexander
3. Create new account = Alexander
4. Delete Account = Shubham
5. User home page (user can see messages of users they follow) = Marcus, Alexander, Henry, & Shubham
6. Publish posts to followers  = Alexander
7. Post image with Message = Shubham
8. Delete Post = Marcus and Henry
9. Password Reset = Shubham
10. Users should be able to follow each other = Alexander and Shubham
11. reCAPTCHA = Alexander

# Setup Guide
1. First make sure all your linux packages are up to date.
You can do this in the terminal by first running
`sudo apt update`
followed by,
`sudo apt upgrade`.
Once a prompt pops up, you can just press enter to continue and finish the upgrade process.

2. You now need to install flask and some other packages used by it. You will need to do
`pip3 install flask`,
`pip3 install flask-wtf flask sqlalchemy flask-login`, and lastly
`pip3 install email_validator`.

3. You will need to setup a database file to store the website info, so first do `flask shell` 
to enter the terminal for the installation, then do `db.create_all()` to initialize your database file.

4. Finally, to run the website enter `python3 run.py` and copy paste the URL into your browser!

# Website Intructions
1. At the top of the website, we have a blue navigation bar where you can create your account or login to your account if you already made one.
2. Fill in your information to either login or sign up.
3. Once logged in, you can see your homepage and some menu buttons
   - To create a post, select create post. It will also give you an option to attach an image with your post.
   - To delete your post, find your post you want to delete on the homepage, and use the drop-down menu next to it to delete the post
   - To follow someone, select follow someone and enter their username
   - To unfollow someone, select stop following someone and enter their username
   - To update your password, select update password
   - To logout, select logout
   - To delete your account, select the delete account button

# Acknowledgments
1. Alexander for fixing our merge conflict by implementing .gitignore
2. Alexander and Shubham for helping diagnose WSL and project setup issues, in addition to helping others on their functional requirements

