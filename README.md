# Django back-blog
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c339f23b0d654f458213cca0c34f28a6)](https://app.codacy.com/manual/samirhinojosa/django-back-blog?utm_source=github.com&utm_medium=referral&utm_content=samirhinojosa/django-back-blog&utm_campaign=Badge_Grade_Dashboard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Simple **Backend** and **Back-office** application for managing a **blog** through Django framework

## Development and Contributing

If you would like to contribute with the project, below you'll see how to start it with docker.
1.  Install Docker and Docker Compose.
2.  In the root of the project's directory run in shell, the command
```
docker-compose up
```
3.  In another shell, do the migrations:
```
python manage.py makemigrations
python manage.py migrate
```
4.  Create an admin user
```
python manage.py createsuperuser
```

Django back-blog is an open source project, so contributing is as easy as forking the project on either of these sites and committing your enhancements. Please, don't forget include always tests. If you are fixing a bug, add a test that breaks before your patch and works after.