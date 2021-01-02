# Mechanic
Mechanic is an E-Commerce website built with Django.

<p align="center">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/maziokey/mechanic">

<img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/okeymaxi?style=flat-square">

</p>


## Project Summary
Mechanic is an E-Commerce website designed for the sale of car spare parts. Users can search for car parts using the make, model, production year, engine type and fuel type of the car. They can select the quantity of each part they intend to buy. Payment processing is handled by Stripe.

## Running this Project
To get this project up and running you should start by having Python3 installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. 
1. I used pipenv and docker for this project. You can install pipenv with:

   ```
   pip3 install pipenv
   ```

1. Fork the project and then run the following commands in the directory of the project.

   ```
   pipenv install
   ```

1. Pipenv will read the Pipfile and Pipfile.lock files for the project, create the virtual environment, and install all of the dependencies as needed. Then run the following commands:

   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
