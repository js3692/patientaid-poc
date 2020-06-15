from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

from config import DATABASE_CONNECTION_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def test():
    db.create_all()

    query_string = text('''
        SELECT CONCAT(table_schema,'.',table_name)
        FROM information_schema.tables
        WHERE table_schema = 'ebdb'
    ''')

    rows = db.engine.execute(query_string)

    # Return the page with the result.
    return render_template('index.html', rows=rows)
