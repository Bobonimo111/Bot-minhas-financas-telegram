from database.Connection import Connection
from database.User import User

conn = Connection()

user = User(id_telegram="11233456")
conn.save(user)
