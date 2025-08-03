# 🧮 Django Calculator App

A beginner-friendly calculator web application built with **Django** and **Bootstrap 5**. This project allows users to evaluate basic Python-style mathematical expressions in a clean, modern interface.

> ⚠️ **Note:** This version uses Python’s built-in `eval()` for evaluation, which is not safe for untrusted input. This project is intended for educational/demo purposes only.

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
git clone https://github.com/your-username/django-calculator.git
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

⚠️ Important Security Note
This app uses the following logic to evaluate user input:
q = request.GET.get('query')
answer = eval(q)  # Not safe for untrusted input!
This can lead to code injection vulnerabilities if deployed online.
✅ For production, replace eval() with secure alternatives like:

ast.literal_eval (only supports simple literals)

Full AST-based arithmetic parsing

Let me know if you want help with this upgrade.

🌟 Possible Future Enhancements
🔐 Safe evaluation using ast (instead of eval)

📊 History stored in database with timestamps

👥 User login system

☁️ Deployment on Heroku or Render

✅ Unit testing for expression logic

🙋 Author
Vivek Sharma
Made with ❤️ using Django and Bootstrap

📜 License
This project is open-source and available under the MIT License.


### ✅ What's Included:
- Fully documented features
- Accurate tech used (eval + Django)
- Security warning for `eval()`
- Step-by-step setup instructions
- Future upgrade suggestions
Let me know if you want this saved as a physical `README.md` file or want me to include it in your Django folder directly.


## 📁 Project Structure

