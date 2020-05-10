# A template to bootstrap TNP Backend projects

## Template info, delete after use the template

To start a new project, click on the "Use this template" button.

The `project` folder is where the main configuration will go. Rename the folder and files to match real project name

It is advisable to create the rest of the apps in the project in an `app` folder with the next command:

`django-admin startproject`

And the structure of the project will remain as follows

- app/app1
- app/app2

# {PROJECT-NAME}

## Installation

### Backend

The backend run in Docker. We need to have docker (docker-engine) and docker-compose installed

To build Docker images (remember that you have to do this everytime you add a new dependency to Pipfile too)

```bash
docker-compose build
```

The first time we start the project locally it will be necessary to migrate the data and create a superuser

```bash
docker-compose run --rm backend pipenv run python manage.py migrate
docker-compose run --rm backend pipenv run python manage.py createsuperuser
```

## Run project

### Start everything (redis, postgress, server, celery and rest of things written in docker-compose.yml)

```bash
docker-compose up
```

## Testing

### Run tests

Always use `{PROJECT-NAME}.settings_test` as Django settings file as we sometimes need to override production settings

```bash
docker-compose run -e DJANGO_SETTINGS_MODULE={PROJECT-NAME}.settings_test --rm backend pipenv run coverage run --source='.' manage.py test
```

### Generate HTML test coverage

```bash
docker-compose run --rm backend pipenv run coverage html
```

### View HTML test coverage

```bash
cd htmlcov
npx http-server
```

Open `localhost:8080` in your browser
