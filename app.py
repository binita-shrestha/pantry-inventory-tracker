from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
def get_db_connection():
    connection = sqlite3.connect("database/pantry.db")
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/inventory")
def inventory_page():
    connection = get_db_connection()

    items = connection.execute("""
        SELECT * FROM inventory
        ORDER BY expiration_date ASC
    """).fetchall()

    connection.close()
    return render_template("inventory.html", items=items)

@app.route("/add", methods=["GET", "POST"])
def add():
    errors = []

    if request.method == "POST":
        item_name = request.form["item_name"].strip()
        category = request.form["category"]
        quantity = request.form["quantity"]
        date_received = request.form["date_received"]
        expiration_date = request.form["expiration_date"]
        minimum_stock = request.form["minimum_stock"]

        if item_name == "":
            errors.append("Item name is required.")

        if category == "":
            errors.append("Category is required.")

        if quantity == "":
            errors.append("Quantity is required.")
        elif int(quantity) < 0:
            errors.append("Quantity cannot be negative.")

        if date_received == "":
            errors.append("Date received is required.")

        if expiration_date == "":
            errors.append("Expiration date is required.")

        if minimum_stock == "":
            errors.append("Minimum stock level is required.")
        elif int(minimum_stock) < 0:
            errors.append("Minimum stock level cannot be negative.")

        if errors:
            return render_template("add.html", errors=errors)

        connection = get_db_connection()

        connection.execute("""
            INSERT INTO inventory 
            (item_name, category, quantity, date_received, expiration_date, minimum_stock)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            item_name,
            category,
            int(quantity),
            date_received,
            expiration_date,
            int(minimum_stock)
        ))

        connection.commit()
        connection.close()

        return redirect(url_for("inventory_page"))

    return render_template("add.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

if __name__ == "__main__":
    app.run(debug=True)