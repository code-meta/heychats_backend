This is the backend of the heychats web app. [frontend preview image](https://raw.githubusercontent.com/code-meta/heychats-frontend/main/public/heychats-preview.png) 


## Prerequisites to run this project
* [Docker](https://www.docker.com/products/docker-desktop/)


## Getting Started
to build the project:
```bash
docker-compose build web
```
to install and run mysql database:
```bash
docker-compose up -d mysql
```
to install and run redis:
```bash
docker-compose up -d redis
```
to create tables in database:
```bash
docker-compose run web python manage.py migrate
```
to create a super user for the app:
```bash
docker-compose run web python manage.py createsuperuser
```
to run the project:
```bash
docker-compose up -d
```

**Once the backend is setup get the [frontend](https://github.com/code-meta/heychats-frontend) of this project.**

this is a realtime chat application the backend is built using django and django-restframework.
and the [frontend](https://github.com/code-meta/heychats-frontend) is built using next.js.