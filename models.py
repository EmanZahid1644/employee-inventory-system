from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'employee_schema'}
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    position = db.Column(db.String(50))
    department = db.Column(db.String(50))
    hire_date = db.Column(db.Date, default=datetime.utcnow)
    salary = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'

class InventoryItem(db.Model):
    __tablename__ = 'inventory_items'
    __table_args__ = {'schema': 'employee_schema'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float)
    supplier = db.Column(db.String(100))
    last_restock = db.Column(db.Date)
    min_stock = db.Column(db.Integer, default=5)
    
    def __repr__(self):
        return f'<InventoryItem {self.name}>'