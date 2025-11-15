# Django project setup steps

## Step 1: Create and Set Up the Project Directory

```bash
# Create project folder
mkdir alx_travel_app
cd alx_travel_app

# Initialize Git repository
git init
```

## Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv
# Activate
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

## Step 3: Install Required Packages

`pip install django djangorestframework django-cors-headers drf-yasg celery django-environ mysqlclient`

### Then export your dependencies to  a file

```bash

pip freeze > requirements.txt

```

## Step 4: Create Django Project and App

```bash
django-admin startproject alx_travel_app .
python manage.py startapp listings
```

## Step 5: Configure `settings.py`

- Open `alx_travel_app/settings.py` and update the following sections

### Add Installed Apps

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'listings',
]
```

### Add Middleware

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', <-- added this
    'django.middleware.common.CommonMiddleware', 
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

### Add CORS Configuration

```python
CORS_ALLOW_ALL_ORIGINS = True

```

## Step 6: Configure `.env` File and Database

- Install **django-environ** (already installed) and create a  `.env` file in the project root

```env
DB_NAME=alx_travel_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306
```

### Update Database in `settings.py`

```python

import environ
import os

env = environ.Env()
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
```

## Step 7: Configure Swagger (`urls.py`)

- Open `alx_travel_app/urls.py` and add Swagger routes

```python
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="API documentation for ALX Travel App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
```

- Now, you’ll be able to access Swagger docs at  
- [[http://127.0.0.1:8000/swagger/]]

## Step 8: Run Initial Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
