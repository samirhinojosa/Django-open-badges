# Django Open Badges
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5cd2f08bf1484f4886b61dc09e113586)](https://www.codacy.com/manual/samirhinojosa/django-open-badges?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=samirhinojosa/django-open-badges&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/samirhinojosa/Django-open-badges.svg?branch=master)](https://travis-ci.org/samirhinojosa/Django-open-badges)
[![Coverage Status](https://coveralls.io/repos/github/samirhinojosa/Django-open-badges/badge.svg?branch=master)](https://coveralls.io/github/samirhinojosa/Django-open-badges?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple **Backend** and **Back-office** application to manage the creation and granting of badges, certificates and credentials through Django framework

## Development and Contributing

If you would like to contribute with the project, below you'll see how to start it with docker.
1.  Install Docker and Docker Compose
2.  In the root of the project's directory run in shell, the command
```docker
docker-compose up
```
3.  In another shell, prepare the migrations based on the apps
```python
python manage.py makemigrations core
python manage.py makemigrations diplomas
```
4.  Make the migrations in the order below. 
```python
python manage.py migrate core
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate admin
python manage.py migrate sessions
python manage.py migrate diplomas
```
5.  Create an admin user
```python
python manage.py createsuperuser
```

### With Visual Studio Code - Insiders
1.  Install Docker and Docker Compose
2.  Open the project with VSC - Insiders
3.  In a bash in VSC's terminal, prepare the migrations based on the apps
```python
python manage.py makemigrations core
python manage.py makemigrations diplomas
```
4.  Make the migrations in the order below. 
```python
python manage.py migrate core
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate admin
python manage.py migrate sessions
python manage.py migrate diplomas
```
5.  Create an admin user
```python
python manage.py createsuperuser
```

## Unit Test - Coverage

To run coverage, execute the command below
```python
coverage run --source='.' manage.py test apps
```
---
**Django Open Badges**  is an open source project, so contributing is as easy as forking the project on either of these sites and committing your enhancements. Please, don't forget include always tests. If you are fixing a bug, add a test that breaks before your patch and works after.
