# 🧮 Django Calculator App !!!

A beginner-friendly calculator web application built with **Django** and **Bootstrap 5**. This project allows users to evaluate basic Python-style mathematical expressions in a clean, modern interface.

---

## 🚀 Features
 
- ✅ Evaluate Python-style arithmetic expressions like `(2+3)*5`
- 🌈 Clean, mobile-responsive UI using **Bootstrap 5**
- 🌙 Toggleable **Dark Mode**
- 🕓 Recent calculation history stored in **sessions**
- 🔢 Supports all basic math operators:
  - `+`, `-`, `*`, `/`, `%`, `**`, `()`

---

## 📋 Sample Input Expressions

| Input Expression | Description      |
|------------------|------------------|
| `2 + 3`          | Addition          |
| `10 - 4`         | Subtraction       |
| `4 * 5`          | Multiplication    |
| `10 / 2`         | Division          |
| `10 % 3`         | Modulus           |
| `2 ** 3`         | Exponentiation    |
| `(2 + 3) * 4`    | Grouping          |

---
django-calculator/
├── calculator/
│ ├── templates/
│ │ └── index.html # Main HTML UI
│ ├── views.py # Core logic (with eval)
│ └── urls.py # URL mapping
├── static/
│ └── logo.png # App logo image
├── manage.py
└── README.md


---

## ⚙️ Tech Stack

- **Backend**: Django 4+
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Session**: Django's session framework (for history)
- **Theme**: Light & Dark Mode with `localStorage` toggle

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/vivek1m/django-calculator.git
cd django-calculator
2. Create and Activate a Virtual Environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3. Install Required Dependencies
pip install django
4. Run the Django Development Server
python manage.py runserver
Visit the app in your browser at:
http://127.0.0.1:8000


Made with ❤️ using Django and Bootstrap
