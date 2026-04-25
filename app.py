from flask import Flask, render_template, request
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
    if request.method == "POST":
        item_name = request.form["item_name"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])
        date_received = request.form["date_received"]
        expiration_date = request.form["expiration_date"]
        minimum_stock = int(request.form["minimum_stock"])

        connection = get_db_connection()
        connection.execute("""
            INSERT INTO inventory 
            (item_name, category, quantity, date_received, expiration_date, minimum_stock)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (item_name, category, quantity, date_received, expiration_date, minimum_stock))
        connection.commit()
        connection.close()
    return render_template("add.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

if __name__ == "__main__":
    app.run(debug=True)