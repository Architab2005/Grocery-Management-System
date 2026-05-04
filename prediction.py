# prediction.py
import mysql.connector
import numpy as np
from config import DB_CONFIG


def get_sales_data(product_name=None):
    conn = mysql.connector.connect(**DB_CONFIG)
    c = conn.cursor()

    if product_name:
        q = """
            SELECT DATE(bill_date), SUM(quantity)
            FROM bill_items
            WHERE product_name = %s
            GROUP BY DATE(bill_date)
            ORDER BY bill_date
        """
        c.execute(q, (product_name,))
    else:
        q = """
            SELECT DATE(bill_date), SUM(quantity)
            FROM bill_items
            GROUP BY DATE(bill_date)
            ORDER BY bill_date
        """
        c.execute(q)

    data = c.fetchall()
    conn.close()
    return data


def predict_demand_simple(product_name, days=7):
    """
    Simple moving‑average prediction for next `days` days.
    """
    data = get_sales_data(product_name)

    if not data:
        return 0

    recent = data[-14:]  # Last 14 days
    if len(recent) < 2:
        return 0

    recent_sales = [row[1] for row in recent]
    avg = np.mean(recent_sales)

    return avg * days


# Example usage
if __name__ == "__main__":
    demand = predict_demand_simple("Milk", days=7)
    print(f"Predicted demand for Milk next 7 days: {demand:.2f} units")