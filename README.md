📦 Pantry Inventory Tracker
📌 Project Overview

The Pantry Inventory Tracker is a web-based application developed to help small community organizations manage donated goods efficiently. This system replaces manual paper-based tracking with a centralized digital solution.

The application allows users to add, view, update, and delete inventory items while monitoring stock levels and expiration dates.

🏢 Organization

Helping Hands Community Pantry
A non-profit organization that collects and distributes food to community members in need.

🎯 Features
Add new inventory items
View all inventory items
Edit existing items
Delete items from inventory
Track low stock items
Track expired items
Track items expiring soon
Input validation and error handling
🛠️ Technologies Used
Frontend: HTML, CSS
Backend: Python (Flask)
Database: SQLite
Version Control: Git & GitHub
📂 Project Structure
pantry-inventory-tracker/
│
├── app/
│   ├── templates/
│   ├── static/
│
├── database/
│   └── pantry.db (auto-generated)
│
├── app.py
├── database_setup.py
├── requirements.txt
├── README.md
└── .gitignore
⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/binita-shrestha/pantry-inventory-tracker.git
cd pantry-inventory-tracker
2. Activate virtual environment
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Create the database
python database_setup.py
5. Run the application
python app.py
6. Open in browser
http://127.0.0.1:5000
🧪 How to Use
Go to Add Item
Enter item details and submit
Go to Inventory to view items
Edit or delete items as needed
Visit Alerts to check:
Low stock items
Expired items
Expiring soon items
⚠️ Notes
The database file (pantry.db) is automatically created and is not included in the repository.
Run database_setup.py before starting the application.
👥 Team
Team Lead: Binita Shrestha
Team Members: Jesus Hernandez Vargas & Ravi Kiran Dasari

📄 License

This project is developed for academic purposes as part of a Software Engineering course.