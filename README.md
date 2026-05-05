# Grocery Management System (GUI)

A simple Tkinter‑based GUI for managing a grocery shop, backed by a MySQL database.  
You can add/view/search customers, products, and staff, generate bills, and display a basic stock report.

## Features
- Add and view customer details (name, phone, cost).
- Add and view product details (name, cost).
- Add and view staff details (name, work, age, salary, phone).
- Search by name for customer, product, or staff.
- Billing system to record sales and customer bills.
- Show stock report from `test.txt` (optional).

## Requirements
- Python 3.x
- MySQL (e.g., XAMPP, WAMP, or standalone MySQL)
- `mysql-connector-python` (installed via `requirements.txt`)
- Tkinter (built‑in in Python)

## Setup

1. **Install Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create MySQL database and tables:**
   Open MySQL and run:
   ```sql
   CREATE DATABASE grocerymanagementsystem;
   USE grocerymanagementsystem;

   CREATE TABLE customer_details(
       phone_no int(13),
       cust_name varchar(25),
       cost float(10)
   );

   CREATE TABLE product_details(
       product_name varchar(25),
       product_cost float(10)
   );

   CREATE TABLE worker_details(
       staff_name varchar(25),
       staff_work varchar(10),
       staff_age int(3),
       staff_salary float(10),
       phone_no int(13)
   );

   CREATE TABLE bill_items (
       id INT AUTO_INCREMENT PRIMARY KEY,
       cust_name VARCHAR(25),
       product_name VARCHAR(25),
       quantity INT,
       unit_price FLOAT,
       total FLOAT,
       bill_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **Configure database credentials:**
   In `config.py`, set your MySQL details:
   ```python
   DB_CONFIG = {
       'host': 'localhost',
       'user': 'root',
       'passwd': 'your_mysql_password',
       'database': 'grocerymanagementsystem'
   }
   ```

4. **Add stock file :**
   Create `test.txt` in the project root if you want to test the stock report.

## How to Run

```bash
python main_gui.py
```

### Login
- Username: `asql`
- Password: `your_password`

After login, use the menu buttons to:
- Add/view/search customers, products, and staff.
- Use the billing module (via new “Generate Bill” / “Billing” menu) to record sales.
- View stock report from `test.txt`.

## 📄 License
This project is licensed under the MIT License.