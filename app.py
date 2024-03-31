from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

# Retrieve the database URL from the environment variable DATABASE_URL
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://myuser:mypassword@database:5432/mydb')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@database:5432/mydb'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    rollnumber = db.Column(db.String(255))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        roll_number = request.form['roll_number']
        student = Student(name=name, rollnumber=roll_number)
        db.session.add(student)
        db.session.commit()
        return redirect('/students')
    return render_template('index.html')

@app.route('/students')
def students():
    student_data = Student.query.all()
    return render_template('students.html', students=student_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database table
    app.run(host='0.0.0.0', port=8080)