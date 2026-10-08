# ✈️ Flight Management System

## 📌 Project Overview

The **Flight Management System** is a web-based application developed using **Python and Django**. It is designed to manage flight-related information and provide an easy-to-use interface for handling flight operations and data.

## 🚀 Features

* ✈️ Flight management
* 👤 User management
* 🛫 Flight information
* 🛬 Booking management
* 🔐 User authentication
* 📝 Form handling and validation
* 📊 Database management
* ⚙️ CRUD operations
* 🖥️ User-friendly interface
* 🔧 Django admin panel

## 🛠️ Technologies Used

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **SQLite**

## 📂 Project Structure

```text
Flight-Management-System/
│
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── ...
│
├── static/
│   ├── css/
│
└── flight_app/
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── ...
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/adityaranjanswain01-tech/Flight-Management-System.git
```

### 2. Navigate to the Project

```bash
cd Flight-Management-System
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
myenv\Scripts\activate
```

**Linux/macOS:**

```bash
source myenv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## 🔐 Admin Panel

The Django admin panel can be accessed at:

```text
http://127.0.0.1:8000/admin/
```

Use the superuser credentials created during installation to log in.

## 🗄️ Database

The project uses **SQLite** as the development database.

Run migrations using:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 📦 Requirements

The required Python packages are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

## 🔒 .gitignore

The following files and folders should not be uploaded to GitHub:

```text
myenv/
venv/
__pycache__/
*.pyc
db.sqlite3
.env
.vscode/
```

## 🎯 Future Improvements

* Online flight booking
* Payment gateway integration
* Email notifications
* Flight search and filtering
* Ticket cancellation
* Passenger history
* Real-time flight status
* Improved responsive design

## 👨‍💻 Author
**Jyotiraditya Ranjan Swain**

GitHub: [@adityaranjanswain01-tech](https://github.com/adityaranjanswain01-tech)
