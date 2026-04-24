from flask import Flask, render_template, request
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
inventory = []

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/inventory")
def inventory_page():
    return render_template("inventory.html", items=inventory)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        item_name = request.form["item_name"]
        category = request.form["category"]
        quantity = int(request.form["quantity"])
        date_received = request.form["date_received"]
        expiration_date = request.form["expiration_date"]
        minimum_stock = int(request.form["minimum_stock"])

        item = {
        "item_name": item_name,
        "category": category,
        "quantity": quantity,
        "date_received": date_received,
        "expiration_date": expiration_date,
        "minimum_stock": minimum_stock
        }

        inventory.append(item)

    return render_template("add.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

if __name__ == "__main__":
    app.run(debug=True)