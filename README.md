# Campus Parking Finder

## Overview
This application helps users quickly find available parking near their desired campus locations. Users can reserve parking spaces and access real-time analytics to see which spots will become available shortly.

---

## Features
- Locate available parking spaces near your desired location  
- Reserve parking spaces 
- View real-time availability of parking spots  

---

## Prerequisites
- Python 
- Django
- SQL
- HTML
- CSS

---

## Setup Instructions


### 1. Clone the Repository
```
git clone <your-repo-url>
cd <your-project-folder>
```
### 2. Dependency / Package Issues
If you experience missing or inconsistent packages, install the required dependencies:
```
pip install -r requirements.txt
```

### 3. Database Setup & Issues
If you encounter database-related errors (missing tables or issues inserting data), run the following commands to create and apply the database migrations:
```
python manage.py makemigrations
python manage.py migrate
```
### 4. Running the Development Server
To start the application and view it in your browser, run:
```
python manage.py runserver
```
## Admin Side
To access admin side of application, first create an admin account for yourself by calling
```
python manage.py createsuperuser
```
Enter in the login details you want for your admin account.
Then, start the app with
```
python manage.py runserver
```
If you visit 127.0.0.1:8000/admin/, you will now be prompted to log-in with your admin account.
