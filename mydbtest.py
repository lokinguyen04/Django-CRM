import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    db="CRM_app",
    port=3307  # <-- Must match
)

print("Database version:", db.get_server_info())
