# main_gui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
from config import DB_CONFIG


class GroceryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery Management System [GUI]")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        self.conn = None
        self.cursor = None

        # Login screen
        self.login_screen()

    def login_screen(self):
        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.login_frame.pack(fill="both", expand=True, padx=20, pady=60)

        tk.Label(self.login_frame, text="Grocery Management System",
                 font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(self.login_frame, text="Username:", bg="#f0f0f0").pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame, width=25)
        self.username_entry.pack(pady=2)

        tk.Label(self.login_frame, text="Password:", bg="#f0f0f0").pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, width=25, show="*")
        self.password_entry.pack(pady=2)

        tk.Button(self.login_frame, text="Login", width=20, bg="green", fg="white",
                  command=self.attempt_login).pack(pady=15)

    def attempt_login(self):
        user = self.username_entry.get()
        pwd = self.password_entry.get()

        if user == "asql" and pwd == "your password":
            self.login_frame.destroy()
            try:
                self.conn = mysql.connector.connect(**DB_CONFIG)
                self.cursor = self.conn.cursor()
                self.menu_screen()
            except Exception as e:
                messagebox.showerror("Database Error", f"Connection failed:\n{e}")
        else:
            messagebox.showerror("Error", "Wrong password, try again.")

    def menu_screen(self):
        self.menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.menu_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tk.Label(self.menu_frame, text="Grocery Management Menu",
                 font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        buttons = [
            ("Add Customer", self.add_customer),
            ("Add Product", self.add_product),
            ("Add Staff", self.add_staff),
            ("View All Customers", self.view_all_customers),
            ("View All Products", self.view_all_products),
            ("View All Staff", self.view_all_staff),
            ("Search Customer", self.search_customer),
            ("Search Product", self.search_product),
            ("Search Staff", self.search_staff),
            ("Stock Report", self.show_stock),
            ("Exit", self.root.destroy),
        ]

        for text, command in buttons:
            tk.Button(self.menu_frame, text=text, width=25, pady=5,
                      command=command).pack(pady=4)

    # === Customer Section ===
    def add_customer(self):
        name = simpledialog.askstring("Add Customer", "Enter customer name:")
        phone = simpledialog.askstring("Add Customer", "Enter phone number:")
        cost = simpledialog.askstring("Add Customer", "Enter cost:")

        if not (name and phone and cost):
            return

        try:
            self.cursor.execute(
                "INSERT INTO customer_details (phone_no, cust_name, cost) VALUES (%s, %s, %s)",
                (int(phone), name, float(cost))
            )
            self.conn.commit()
            messagebox.showinfo("Success", "Customer added.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add customer:\n{e}")

    def view_all_customers(self):
        try:
            self.cursor.execute("SELECT * FROM customer_details")
            records = self.cursor.fetchall()
            msg = "\n".join([f"Phone: {r[0]}, Name: {r[1]}, Cost: {r[2]}" for r in records])
            messagebox.showinfo("All Customers", msg or "No customers found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch customers:\n{e}")

    def search_customer(self):
        name = simpledialog.askstring("Search Customer", "Enter customer name:")
        if not name:
            return
        try:
            self.cursor.execute("SELECT * FROM customer_details WHERE cust_name = %s", (name,))
            records = self.cursor.fetchall()
            msg = "\n".join([f"Phone: {r[0]}, Name: {r[1]}, Cost: {r[2]}" for r in records])
            messagebox.showinfo("Customer Result", msg or "No customer found.")
        except Exception as e:
            messagebox.showerror("Error", f"Search failed:\n{e}")

    # === Product Section ===
    def add_product(self):
        name = simpledialog.askstring("Add Product", "Enter product name:")
        cost = simpledialog.askstring("Add Product", "Enter cost:")

        if not (name and cost):
            return

        try:
            self.cursor.execute(
                "INSERT INTO product_details (product_name, product_cost) VALUES (%s, %s)",
                (name, float(cost))
            )
            self.conn.commit()
            messagebox.showinfo("Success", "Product added.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add product:\n{e}")

    def view_all_products(self):
        try:
            self.cursor.execute("SELECT * FROM product_details")
            records = self.cursor.fetchall()
            msg = "\n".join([f"Name: {r[0]}, Cost: {r[1]}" for r in records])
            messagebox.showinfo("All Products", msg or "No products found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch products:\n{e}")

    def search_product(self):
        name = simpledialog.askstring("Search Product", "Enter product name:")
        if not name:
            return
        try:
            self.cursor.execute("SELECT * FROM product_details WHERE product_name = %s", (name,))
            records = self.cursor.fetchall()
            msg = "\n".join([f"Name: {r[0]}, Cost: {r[1]}" for r in records])
            messagebox.showinfo("Product Result", msg or "No product found.")
        except Exception as e:
            messagebox.showerror("Error", f"Search failed:\n{e}")

    # === Staff Section ===
    def add_staff(self):
        name = simpledialog.askstring("Add Staff", "Enter staff name:")
        work = simpledialog.askstring("Add Staff", "Enter work:")
        age = simpledialog.askstring("Add Staff", "Enter age:")
        salary = simpledialog.askstring("Add Staff", "Enter salary:")
        phone = simpledialog.askstring("Add Staff", "Enter phone:")

        if not all([name, work, age, salary, phone]):
            return

        try:
            self.cursor.execute(
                "INSERT INTO worker_details (staff_name, staff_work, staff_age, staff_salary, phone_no) "
                "VALUES (%s, %s, %s, %s, %s)",
                (name, work, int(age), float(salary), int(phone))
            )
            self.conn.commit()
            messagebox.showinfo("Success", "Staff added.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add staff:\n{e}")

    def view_all_staff(self):
        try:
            self.cursor.execute("SELECT * FROM worker_details")
            records = self.cursor.fetchall()
            msg = "\n".join([f"Name: {r[0]}, Work: {r[1]}, Age: {r[2]}, Salary: {r[3]}, Phone: {r[4]}"
                            for r in records])
            messagebox.showinfo("All Staff", msg or "No staff found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch staff:\n{e}")

    def search_staff(self):
        name = simpledialog.askstring("Search Staff", "Enter staff name:")
        if not name:
            return
        try:
            self.cursor.execute("SELECT * FROM worker_details WHERE staff_name = %s", (name,))
            records = self.cursor.fetchall()
            msg = "\n".join([f"Name: {r[0]}, Work: {r[1]}, Age: {r[2]}, Salary: {r[3]}, Phone: {r[4]}"
                            for r in records])
            messagebox.showinfo("Staff Result", msg or "No staff found.")
        except Exception as e:
            messagebox.showerror("Error", f"Search failed:\n{e}")

    # === Stock (file read) ===
    def show_stock(self):
        try:
            with open("test.txt", "r") as f:
                data = f.read()
            messagebox.showinfo("Stock Report", data or "No stock data.")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "test.txt not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Cannot read file:\n{e}")

    def __del__(self):
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryGUI(root)
    root.mainloop()