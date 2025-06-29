# 🧠 MCQ Test App – Django Based Quiz System

A clean and functional **multiple-choice question (MCQ) test interface** built using Django, developed as part of my portfolio for college and placement preparation.

> 🎯 Built for MGM's JNEC Aurangabad | GATE Prep | Final Year Projects | Campus Placements

---

## 🚀 Features

- 🔹 Displays MCQ questions with 4 options
- 🔹 Shows immediate feedback (Correct/Wrong)
- 🔹 Displays correct answer and explanation
- 🔹 Admin interface to add/manage questions
- 🔹 Modular template system with `base.html`, `header.html`, sidebars, and main content
- 🔹 Mobile-friendly, minimal design
- 🔹 Designed to run fast on low-end machines

---

## ⚙️ How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/akashch1512/Prep_Tester.git
   cd mcq-test-app


2. **Create virtual environment (optional but recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**

   ```bash
   python manage.py runserver
   ```

7. **Access the app**

   * Test Interface: `http://127.0.0.1:8000/`
   * Admin Panel: `http://127.0.0.1:8000/admin/`

---

```markdown
Prep_Tester/
├── mcq/ # Django app (questions, views, models)
├── templates/
│ ├── base.html # Master layout
│ ├── header.html # Top navbar
│ ├── sidebar_left.html
│ ├── sidebar_right.html
│ └── question.html # Test interface
├── static/ # (Optional) CSS / JS / assets
├── db.sqlite3 # Default database
└── manage.py
````
## 🧩 Model Overview

```python
class Question(models.Model):
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()  # 1 to 4
    solution = models.TextField()
```

---

## 📌 Notes

* This project is a **starter interface** for any quiz/test application.
* Future additions may include:

  * User login/session tracking
  * Question bank upload via CSV
  * Timed tests
  * Scoring system and analytics
