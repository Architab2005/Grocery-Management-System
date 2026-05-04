# dashboard.py
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
from config import DB_CONFIG
from prediction import predict_demand_simple


class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Analytics Dashboard")
        self.root.geometry("1000x700")

        self.sales_data = self.get_daily_sales()
        self.top_products = self.get_top_products()

        self.create_ui()

    def get_daily_sales(self):
        conn = mysql.connector.connect(**DB_CONFIG)
        c = conn.cursor()
        c.execute("""
            SELECT DATE(bill_date), SUM(total)
            FROM bill_items
            GROUP BY DATE(bill_date)
            ORDER BY bill_date
        """)
        data = c.fetchall()
        conn.close()
        return data

    def get_top_products(self, limit=5):
        conn = mysql.connector.connect(**DB_CONFIG)
        c = conn.cursor()
        c.execute("""
            SELECT product_name, SUM(quantity) AS total_sold
            FROM bill_items
            GROUP BY product_name
            ORDER BY total_sold DESC
            LIMIT %s
        """, (limit,))
        data = c.fetchall()
        conn.close()
        return data

    def create_ui(self):
        tk.Label(self.root, text="Admin Analytics Dashboard",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tabs = ttk.Notebook(self.root)
        tabs.pack(fill="both", expand=True, padx=10, pady=10)

                # Tab 1: Sales Over Time
        tab1 = tk.Frame(tabs)
        tabs.add(tab1, text="Sales Over Time")

        fig1, ax1 = plt.subplots(figsize=(8, 4))
        if self.sales_data:
            dates = [row[0] for row in self.sales_data]
            sales = [row[1] for row in self.sales_data]
            ax1.plot(dates, sales, marker="o")
            ax1.set_title("Daily Sales")
            ax1.set_xlabel("Date")
            ax1.set_ylabel("Sales (₹)")

        canvas1 = FigureCanvasTkAgg(fig1, tab1)
        canvas1.get_tk_widget().pack(fill="both", expand=True)

        # Tab 2: Top Products
        tab2 = tk.Frame(tabs)
        tabs.add(tab2, text="Top Products")

        tk.Label(tab2, text="Top Products (by quantity sold)", font=("Arial", 12)).pack(pady=5)
        for product, qty in self.top_products:
            tk.Label(tab2, text=f"{product}: {qty:.0f} units").pack(anchor="w", padx=10)

        # Tab 3: Inventory Prediction
        tab3 = tk.Frame(tabs)
        tabs.add(tab3, text="Inventory Prediction")

        tk.Label(tab3, text="Inventory Prediction (next 7 days)", font=("Arial", 12)).pack(pady=5)

        products = ["Milk", "Bread", "Butter", "Rice", "Pulses"]  # configurable
        for p in products:
            demand = predict_demand_simple(p, days=7)
            tk.Label(tab3, text=f"{p}: {demand:.2f} units").pack(anchor="w", padx=10)

        tk.Button(self.root, text="Refresh Data", bg="blue", fg="white",
                  command=self.refresh_data).pack(pady=10)

    def refresh_data(self):
        self.sales_data = self.get_daily_sales()
        self.top_products = self.get_top_products()
        for child in self.root.winfo_children():
            if isinstance(child, ttk.Notebook):
                child.destroy()
        self.create_ui()


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()