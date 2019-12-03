from application import db
from datetime import datetime

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True, unique=False)
    notes = db.Column(db.String(128), index=False, unique=False)
    created_at = db.Column(db.DateTime(), index=True, unique=False)
    completed = db.Column(db.Boolean(), index=True, unique=False)
    
    def __init__(self, title, notes):
        self.title = title
        self.notes = notes
        self.created_at = datetime.now()
        self.completed = False

    def __repr__(self):
        return '<TodoList %r>' % self.title

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'notes': self.notes,
            'created_at': self.created_at,
            'completed': self.completed,
        }