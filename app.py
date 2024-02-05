import os

from flask import Flask, render_template, request
from database import Employee, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["CONNECTION_STRING"]

db.init_app(app)

with app.app_context():
  db.create_all()

@app.route("/<name>", methods=['GET'])
def get_index(name):
  return render_template('index.html', name=name)

@app.route("/api/v1/employees", methods=['GET'])
def get_employees():
  query = db.select(Employee)
  employees = db.session.execute(query).scalars().all()
  return employees

@app.route("/api/v1/employees/<int:id>", methods=['GET'])
def get_employee(id):
  employee = db.get_or_404(Employee, id)
  return [employee]

@app.route("/api/v1/employees", methods=['POST'])
def create_employee():
  employee = Employee(
    username=request.json["username"],
    email=request.json["email"]
  )
  
  db.session.add(employee)
  db.session.commit()

  return f"/api/v1/employees/{employee.id}"

@app.route("/api/v1/employees/<int:id>", methods=['DELETE'])
def delete_employee(id):
  employee = db.get_or_404(Employee, id)
  db.session.delete(employee)
  db.session.commit()
  return f"Deleted employee {id}"