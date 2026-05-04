# billing.py
import mysql.connector
from config import DB_CONFIG


def create_bill(customer_name, phone_no, items):
    """
    items = [ (product_name, quantity, unit_price), ... ]
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        c = conn.cursor()

        total_amount = 0

        # 1. Insert customer if not exists
        c.execute(
            "INSERT IGNORE INTO customer_details (phone_no, cust_name, cost) VALUES (%s, %s, 0.0)",
            (phone_no, customer_name)
        )

        # 2. Record each item sale
        for product_name, qty, unit_price in items:
            total_amount += qty * unit_price

            c.execute(
                "INSERT INTO bill_items (cust_name, product_name, quantity, unit_price, total) "
                "VALUES (%s, %s, %s, %s, %s)",
                (customer_name, product_name, qty, unit_price, qty * unit_price)
            )

        # 3. Update customer total
        c.execute(
            "UPDATE customer_details SET cost = cost + %s WHERE phone_no = %s",
            (total_amount, phone_no)
        )

        conn.commit()
        conn.close()

        return {
            "customer": customer_name,
            "phone": phone_no,
            "items": items,
            "total": total_amount
        }

    except Exception as e:
        print("Billing error:", e)
        return None


# Example (for testing)
if __name__ == "__main__":
    items = [("Milk", 2, 45.0), ("Bread", 1, 30.0)]
    bill = create_bill("Rahul", 9876543210, items)
    print("Generated bill:", bill)