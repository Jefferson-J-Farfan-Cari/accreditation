# Accreditation System
This project was build with Django, Django-RestFramework, PostgreSQL
### Installation
- This project works with Django, Django Rest Framework, and PostgreSQL Database

**1. Clone the project**
~~~  
https://github.com/Jefferson-J-Farfan-Cari/accreditation.git
~~~

### Execution of project

**1. Run backend development server**   
- Is necessary make a new copy of **.env** file in:
~~~
backend/accreditation/settings
~~~
- Create a virtual environment to python [venv]:
~~~
python -m venv ./venv
~~~
- Activate virtual environment
~~~
venv\Scripts\activate
~~~
- Install all required dependencies for the project:
~~~
pip install -r requirements.txt
~~~
- Make migrations:
~~~
python manage.py makemigrations --settings=accreditation.settings.dev
python manage.py migrate --settings=accreditation.settings.dev --run-syncdb
~~~
- Create Superuser:
~~~
python manage.py createsuperuser --settings=accreditation.settings.dev
~~~
- Start backend development server.
~~~
python manage.py runserver --settings=accreditation.settings.dev
~~~
- The backend project must be running in http://localhost:8000/
- Admin must be running in http://localhost:8000/admin
- Swagger must be running in http://localhost:8000/swagger/
- Redoc documentation must be running in http://localhost:8000/redoc/
