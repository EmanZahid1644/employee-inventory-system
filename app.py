from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Employee, InventoryItem
from config import config
from datetime import datetime
import os

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Updated database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://emanzahid1644:newpassword@localhost/employee_inventory'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize db before migrate
    db.init_app(app)
    migrate = Migrate(app, db)
    # Register blueprints or add routes here
    
    @app.route('/')
    def dashboard():
        employees = Employee.query.filter_by(is_active=True).all()
        inventory = InventoryItem.query.all()
        
        # Calculate stats for dashboard
        total_employees = len(employees)
        total_inventory = sum(item.quantity for item in inventory)
        low_stock_items = [item for item in inventory if item.quantity < item.min_stock]
        
        return render_template('dashboard.html', 
                             employees=employees,
                             inventory=inventory,
                             total_employees=total_employees,
                             total_inventory=total_inventory,
                             low_stock_items=low_stock_items)
    
    @app.route('/employees')
    def employee_list():
        employees = Employee.query.order_by(Employee.last_name).all()
        return render_template('employees.html', employees=employees)
    
    @app.route('/employees/add', methods=['GET', 'POST'])
    def add_employee():
        if request.method == 'POST':
            try:
                employee = Employee(
                    first_name=request.form['first_name'],
                    last_name=request.form['last_name'],
                    email=request.form['email'],
                    phone=request.form.get('phone'),
                    position=request.form.get('position'),
                    department=request.form.get('department'),
                    hire_date=datetime.strptime(request.form['hire_date'], '%Y-%m-%d'),
                    salary=float(request.form.get('salary', 0))
                )
                db.session.add(employee)
                db.session.commit()
                flash('Employee added successfully!', 'success')
                return redirect(url_for('employee_list'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error adding employee: {str(e)}', 'danger')
        
        return render_template('add_employee.html')
    
    @app.route('/employees/<int:id>/edit', methods=['GET', 'POST'])
    def edit_employee(id):
        employee = Employee.query.get_or_404(id)
        
        if request.method == 'POST':
            try:
                employee.first_name = request.form['first_name']
                employee.last_name = request.form['last_name']
                employee.email = request.form['email']
                employee.phone = request.form.get('phone')
                employee.position = request.form.get('position')
                employee.department = request.form.get('department')
                employee.hire_date = datetime.strptime(request.form['hire_date'], '%Y-%m-%d')
                employee.salary = float(request.form.get('salary', 0))
                
                db.session.commit()
                flash('Employee updated successfully!', 'success')
                return redirect(url_for('employee_list'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating employee: {str(e)}', 'danger')
        
        return render_template('edit_employee.html', employee=employee)
    
    @app.route('/employees/<int:id>/delete', methods=['POST'])
    def delete_employee(id):
        employee = Employee.query.get_or_404(id)
        try:
            employee.is_active = False
            db.session.commit()
            flash('Employee deactivated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deactivating employee: {str(e)}', 'danger')
        
        return redirect(url_for('employee_list'))
    
    # Inventory routes (similar pattern to employees)
    @app.route('/inventory')
    def inventory_list():
        items = InventoryItem.query.order_by(InventoryItem.name).all()
        return render_template('inventory.html', items=items)
    
    @app.route('/inventory/add', methods=['GET', 'POST'])
    def add_inventory_item():
        if request.method == 'POST':
            try:
                item = InventoryItem(
                    name=request.form['name'],
                    category=request.form.get('category'),
                    quantity=int(request.form.get('quantity', 0)),
                    price=float(request.form.get('price', 0)),
                    supplier=request.form.get('supplier'),
                    min_stock=int(request.form.get('min_stock', 5)),
                    last_restock=datetime.strptime(request.form['last_restock'], '%Y-%m-%d') if request.form.get('last_restock') else None
                )
                db.session.add(item)
                db.session.commit()
                flash('Inventory item added successfully!', 'success')
                return redirect(url_for('inventory_list'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error adding inventory item: {str(e)}', 'danger')
        
        return render_template('add_inventory.html')
    
    @app.route('/inventory/<int:id>/edit', methods=['GET', 'POST'])
    def edit_inventory_item(id):
        item = InventoryItem.query.get_or_404(id)
        
        if request.method == 'POST':
            try:
                item.name = request.form['name']
                item.category = request.form.get('category')
                item.quantity = int(request.form.get('quantity', 0))
                item.price = float(request.form.get('price', 0))
                item.supplier = request.form.get('supplier')
                item.min_stock = int(request.form.get('min_stock', 5))
                item.last_restock = datetime.strptime(request.form['last_restock'], '%Y-%m-%d') if request.form.get('last_restock') else None
                
                db.session.commit()
                flash('Inventory item updated successfully!', 'success')
                return redirect(url_for('inventory_list'))
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating inventory item: {str(e)}', 'danger')
        
        return render_template('edit_inventory.html', item=item)
    
    @app.route('/inventory/<int:id>/delete', methods=['POST'])
    def delete_inventory_item(id):
        item = InventoryItem.query.get_or_404(id)
        try:
            db.session.delete(item)
            db.session.commit()
            flash('Inventory item deleted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error deleting inventory item: {str(e)}', 'danger')
        
        return redirect(url_for('inventory_list'))
    
    @app.route('/api/dashboard-stats')
    def dashboard_stats():
        employees = Employee.query.filter_by(is_active=True).all()
        inventory = InventoryItem.query.all()
        
        stats = {
            'total_employees': len(employees),
            'total_inventory': sum(item.quantity for item in inventory),
            'low_stock_count': len([item for item in inventory if item.quantity < item.min_stock])
        }
        
        return jsonify(stats)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)