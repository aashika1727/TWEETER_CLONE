
# 🐦 Tweeter Clone – Django Project

A mini Twitter-like web application built with Django and MySQL. Users can register, log in, post tweets (with optional photos), and view other users' profiles. Built for learning full-stack web development using Django.

---

## 🚀 Features

- User registration and login/logout
- Create, read, update, and delete tweets
- Optional image upload with each tweet
- My Account dashboard for personal tweet management
- View public profiles of other users
- Search functionality for tweets
- Admin panel for tweet management

---

## 🔧 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Django Templates, Bootstrap 5
- **Database**: MySQL
- **Media Handling**: Django Media Storage
- **Auth**: Django Built-in Authentication

---

## 📁 Project Structure

```
TWEETER_CLONE/
├── tweet/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
├── TweeterClone/
│   ├── settings.py
│   ├── urls.py
├── media/
├── static/
├── templates/
├── db (MySQL connected)
└── README.md
```

---

## 🛠️ How to Run Locally

1. Clone the repository
2. Create and activate a virtual environment
3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Configure your MySQL DB in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tweeter_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:

```bash
python manage.py createsuperuser
```

7. Run the server:

```bash
python manage.py runserver
```

---

## 👤 Author

- **Your Name**: Aashika Patel  
- **GitHub**: [@aashika1727](https://github.com/aashika1727)
