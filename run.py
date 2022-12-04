from app import myapp_obj

myapp_obj.run(debug = True)

'''
IMPORTANT NOTES
- Packages you need to install
  -pip3 install flask
  -pip3 install flask-wtf flask sqlalchemy flask-login
  -pip3 install email_validator

- Install SQLiteBrowser using one of the methods described in https://sqlitebrowser.org/dl/
  in order to view the database (db) file

- To reset/erase the database, do "flask shell" in the root directory terminal for the project, then "db.create_all()"
'''