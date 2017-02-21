import csv

username = "pjonak"
subfolder = "Examples/"

cfg_db_folderpath = "/export/home/dor/" + username + "/" + subfolder
cfg_db_filepath = "db.cnf"


hFile = open(cfg_db_folderpath + cfg_db_filepath)
dat = csv.reader(hFile, delimiter=',')

host = [None]
port = [None]
database = [None]
user = [None]
password = [None]
for row in dat:
    # row = ['host', 'rhrcssql01.hbs.edu']
    #   row[0] = 'host'
    #   row[1] = 'rhrcssql01.hbs.edu'

    if row[0] == "host":
        host = row[1]
    elif row[0] == "port":
        port = int( row[1] )
    elif row[0] == "database":
        database = row[1]
    elif row[0] == "user" or row[0] == "username":
        user = row[1]
    elif row[0] == "pass" or row[0] == "password":
        password = row[1]

print(host)
print(port)
print(database)
print(user)
print(password)

hFile.close()
