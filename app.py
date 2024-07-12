from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    #To debbugin
    def __repr__(self):
        return f'<Todo {self.id} {self.description}  >'

with app.app_context():
    db.create_all()

#Routes
@app.route('/')
def index():
    data = Todo.query.all()
    return render_template('index.html', data)
