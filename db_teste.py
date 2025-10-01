from database.Connection import Connection
from database import Category , Gasto,User


conn = Connection()

user = User.User(id_telegram="1123345145566")
cat = Category.Category(nome="Mercado")
gasto = Gasto.Gasto(valor="105.55",local="Mercado da esquina",category=cat,user=user)
conn.save(gasto)
