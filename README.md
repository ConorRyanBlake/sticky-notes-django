# Sticky Notes

A simple Django web application for creating, viewing, editing, and deleting sticky notes. Built as part of the HyperionDev AI Engineering Level 2 course.

## Features

- Create new sticky notes with a title and content
- View all notes as a grid of cards on the home page
- Click any note to see its full details
- Edit or delete existing notes
- Automatically timestamps every note on creation

## Tech stack

- Python 3
- Django 5
- Bootstrap 5 (via CDN)
- SQLite (default Django database)

## Setup instructions

### 1. Clone the repository
git clone https://github.com/ConorRyanBlake/sticky-notes-django.git
cd sticky-notes-django

### 2. Create and activate a virtual environment

On Windows:
python -m venv venv
venv\Scripts\activate

### 3. Install the dependencies
pip install -r requirements.txt

### 4. Run database migrations
python manage.py makemigrations
python manage.py migrate

### 5. (Optional) Create a superuser to access the admin panel
python manage.py createsuperuser

### 6. Start the development server
python manage.py runserver

Open your browser at http://127.0.0.1:8000/ and you're in.

## Running the tests

With the venv active:
python manage.py test notes

## Project structure
sticky_notes/
├── manage.py
├── requirements.txt
├── sticky_notes/      # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── notes/             # The notes app
├── models.py      # Note model
├── views.py       # CRUD views
├── forms.py       # Note form
├── urls.py        # URL routing
├── admin.py       # Admin panel config
├── tests.py       # Unit tests
├── templates/     # HTML templates
└── static/        # CSS