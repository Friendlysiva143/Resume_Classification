# 🧾 Resume Classification System

A Machine Learning powered Resume Classification Web Application built using Django.

Upload a resume (PDF or DOCX), and the system predicts the job category along with a confidence score.

---

## 🚀 Features

- 📄 Upload Resume (.pdf / .docx)
- 🔍 Automatic Text Extraction
- 🛡 Resume Validation Logic
- 🤖 ML-Based Classification
- 📊 Confidence Score Display
- 🎨 Clean UI with Navbar & Footer
- ❌ Proper Error Handling

---

## 🧠 Predicted Categories

| Label | Category        |
|-------|-----------------|
| 0     | Peoplesoft      |
| 1     | React JS        |
| 2     | SQL Developer   |
| 3     | Workday         |

---

## 🛠 Tech Stack

- Python
- Django
- Scikit-learn
- Joblib
- HTML / CSS
- pdfplumber (PDF text extraction)
- python-docx (DOCX text extraction)

---

## 📂 Project Structure

resume_project/

│

├── classifier/

│   ├── model/

│   │   └── resume_classifier_tuned.pkl

│   ├── utils.py

│   ├── views.py

│   └── templates/

│       └── upload.html

│

├── manage.py

├── requirements.txt

└── README.md

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository


git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
### 2️⃣ Create Virtual Environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
### 3️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install django scikit-learn joblib pdfplumber python-docx gunicorn whitenoise
### 4️⃣ Apply Migrations
python manage.py migrate
### 5️⃣ Run Development Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000/

```bash