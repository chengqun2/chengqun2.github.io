### create a project called mysite inside the djangotutorial directory
`django-admin startproject mysite djangotutorial`

### start server
`python manage.py runserver`

### visit the url with your web browser
`http://127.0.0.1:8000/`

### Django create admin user
`python manage.py createsuperuser`

### migrate database
`python manage.py makemigrations`
`python manage.py migrate`

### access the database shell for SQLite
`python manage.py dbshell`
`.tables`
`.schema --indent auth_user`
`select * from auth_user;`

### Install Django REST Framework
`pip install djangorestframework`