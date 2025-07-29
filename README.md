Learning Log:
A web application built with Django that allows users to log and track topics they’re learning about. Each topic can have multiple entries, making it easy to document progress over time.

Features:
User authentication (sign up, log in, log out)

Create, edit, and delete topics

Add and manage entries for each topic

Simple, clean user interface

Tech Stack:
Backend: Django (Python)

Database: SQLite3 (for development)

Frontend: HTML, CSS, Bootstrap

Deployment Ready: Render / Heroku

Installation (Local Setup):
Clone the repository:
git clone https://github.com/Bib2003/learning_log.git
cd learning_log
Create a virtual environment & install dependencies:
python -m venv ll_env
ll_env\Scripts\activate   # (Windows)
pip install -r requirements.txt

Run migrations:
python manage.py migrate
Start the development server:


python manage.py runserver
Open http://127.0.0.1:8000 in your browser.

Usage:
Create an account or log in.

Add new learning topics.

Add entries for each topic to document your progress.

License:
This project is open-source and available for personal or educational use.
