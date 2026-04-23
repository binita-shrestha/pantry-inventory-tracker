from flask import Flask, render_template
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/inventory")
def inventory():
    return render_template("inventory.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/alerts")
def alerts():
    return render_template("alerts.html")

if __name__ == "__main__":
    app.run(debug=True)