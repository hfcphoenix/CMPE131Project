from app import myapp_obj

myapp_obj.run(debug = True)

'''
IMPORTANT NOTES
- You need to do "pip3 install email_validator" to install additional package

- To reset/erase the database, do "flask shell" in the root directory terminal for the project, then "db.create_all()"

- Install SQLiteBrowser using one of the methods described in https://sqlitebrowser.org/dl/
  in order to view the database (db) file
'''