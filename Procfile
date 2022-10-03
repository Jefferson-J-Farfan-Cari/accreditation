web: gunicorn accreditation.wsgi

release: python manage.py makemigrations --settings=accreditation.settings.heroku
release: python manage.py migrate --settings=accreditation.settings.heroku --run-syncdb
