# IRL Patch
- Alexander Pereira (@50xp50)
- Shubham Mishra (@shubhammishra-2020) - Team Lead
- Henry Choy (@hfcphoenix)
- Marcus Lang (@MarcoPolo987)

# Functional Requirements Implemented
1. Login = Alexander
2. Logout sceen = Alexander
3. Create new account = Alexander
4. Delete Account = Shubham
5. User home page (user can see messages of users they follow) = Marcus, Alexander, Henry, & Shubham
6. Publish posts to followers  = Alexander
7. Post image with Message = Marcus and Shubham
8. Delete Post = Marcus and Henry
9. Password Reset = Shubham
10. Users should be able to follow each other = Alexander and Shubham
11. reCAPTCHA = Alexander

# Setup Guide

Installing Flask Libraries: 
1. First make sure all your linux packages are up to date.
Run this command first:
`sudo apt update`
next, run:
`sudo apt upgrade`
Finally, just hit enter to finish the installation proccess.

2. Install these packages with your linux terminal:

`pip3 install flask
pip3 install flask-wtf flask sqlalchemy flask-login
pip3 install email_validator
`
3. Install SQLiteBrowser using one of the methods described in https://sqlitebrowser.org/dl/ in order to view the database (db) file

4. To reset/erase the database, enter `flask shell` in the root directory terminal for the project, then `db.create_all()`

5. Finally, to run the website enter `python3 run.py` and copy paste the URL into your browser!

# Website Intructions
1. At the top of the website, we have a blue navigation bar where you can create your account or login to your account if you already made one.
2. Fill in your information to either login or sign up.
3. To create a post, select create post.
4. To add an image with your post, click upload image.
5. To delete your post, select delete post with the dropdown menu.

# Acknowledgments
1. Alexander for fixing our merge conflict by implementing .gitignore
2. Alexander and Shubham for helping diagnose WSL and project setup issues, in addition to helping others on their functional requirements

