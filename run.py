from app import myapp_obj # grab object from init

myapp_obj.run(debug = True) # run website

'''
IMPORTANT NOTES

- To create new database, do "flask shell" in root directory, then db.create_all()

- You need to install "pip3 install email_validator" for additional package

- Install SQLiteBrowser using one of the methods described in https://sqlitebrowser.org/dl/
  in order to view the database

'''