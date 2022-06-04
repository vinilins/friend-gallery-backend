# Friend Gallery Backend

## How does the project organization work?
```
backend <-- Root path
│
│   .pylintrc <-- Here is the pylint code formatting settings
│   .gitignore <-- Here is the paths and files that git will ignorate.
│   .flake8 <-- Here is the flake8 config about the convetional patterns in python
│   .pre-commit-config.yaml <-- Config to run scripts BEFORE committing, eg black. https://pre-commit.com
│   Procfile <-- Config to run the application on Heroku
│   Dockerfile <-- Here is the config about the Docker of the system.
│   install.sh <-- Here has the config that the docker container will use to create the virtual environment, install the requirements and pre-commit.
│
└─── src <-- Here is the business logic, routes, models, etc.
│      └─── auth <-- Authentication and login module.
│      └─── infra <-- Database Settings.
│      └─── photo <-- Photo module.
│              └─── controllers.py <-- Here has the business logic of the photo module
│              └─── models.py <-- Here has the class Photo, that is the model. 
│              └─── repo.py <-- Here has the classes RepoWritePhoto and RepoReadPhoto, that this make the queries and creations on database 
│              └─── resources.py <-- Here has the routes about the photo module.
│      └─── user <-- User module (Same structure of the Photo Module).
│      └─── tests <-- Here are the system unit tests, which use pytest
│              └─── auth <-- Tests about the auth module.
│              └─── photo <-- Tests about the photo module.
│              └─── user <-- Tests about the user module.
│      └─── app.py <-- File that initialize all modules of the system
│      └─── config.py <-- File about the envs and environments of the system
│      └─── resources.py <-- File that register all routes of the system
```
## How to run the project?