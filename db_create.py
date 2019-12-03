from application import db
from application.models import TodoList

db.create_all()

print("DB created.")