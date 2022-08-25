from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Drink(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route("/drinks")
def get_drinks():
    drinks = Drink.query.all()
    output = []
    for drink in drinks:
        drink_data = {"name": drink.name,"description": drink.description}

    output.append(drink_data)
    return {"drinks": output}
if __name__ == '__main__':
    app.run(debug=True)