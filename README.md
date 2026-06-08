# Employee & Inventory Management System

A web-based Employee and Inventory Management System built with **Flask**, **SQLAlchemy**, **PostgreSQL**, and **Bootstrap**. This application helps organizations manage employee records and inventory items through an easy-to-use dashboard.

## 🚀 Features

### Employee Management

* Add new employees
* Update employee information
* View employee records
* Deactivate employees instead of permanently deleting them
* Manage departments, positions, salaries, and hire dates

### Inventory Management

* Add inventory items
* Edit inventory details
* Delete inventory items
* Track stock quantities
* Monitor low-stock items
* Manage suppliers and restocking dates

### Dashboard

* Total active employees count
* Total inventory quantity
* Low stock alerts
* Real-time statistics API endpoint

### Database Management

* PostgreSQL database integration
* SQLAlchemy ORM
* Flask-Migrate support for database migrations

---

## 🛠️ Technologies Used

* Python
* Flask
* PostgreSQL
* Flask-SQLAlchemy
* Flask-Migrate
* HTML5
* CSS3
* Bootstrap
* Jinja2 Templates

---

## 📂 Project Structure

```text
project/
│
├── app.py
├── models.py
├── config.py
├── requirements.txt
│
├── migrations/
│
├── templates/
│   ├── dashboard.html
│   ├── employees.html
│   ├── add_employee.html
│   ├── edit_employee.html
│   ├── inventory.html
│   ├── add_inventory.html
│   └── edit_inventory.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/employee-inventory-management.git
cd employee-inventory-management
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Create PostgreSQL database:

```sql
CREATE DATABASE employee_inventory;
```

Update database configuration in `app.py` or `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/employee_inventory"
```

Run migrations:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

---

## ▶️ Run the Application

```bash
python app.py
```

Application will be available at:

```text
http://localhost:5000
```

---

## 📊 API Endpoint

### Dashboard Statistics

```http
GET /api/dashboard-stats
```

Example Response:

```json
{
  "total_employees": 15,
  "total_inventory": 250,
  "low_stock_count": 4
}
```

---

## 🔐 Future Improvements

* User Authentication & Authorization
* Employee Attendance Tracking
* Inventory Reports
* Export Data to Excel/PDF
* Role-Based Access Control
* REST API Expansion

---

## 🎯 Learning Objectives

This project demonstrates:

* Flask Application Factory Pattern
* CRUD Operations
* PostgreSQL Integration
* SQLAlchemy ORM
* Database Migrations
* Template Rendering with Jinja2
* REST API Development
* Dashboard Analytics

---

## 👨‍💻 Author

**Eman Zahid**


---

## 📜 License

This project is developed for educational and learning purposes.
