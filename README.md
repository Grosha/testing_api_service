# API tests for service 'Rent car service'

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python 3.7.5
Pip

```
$ brew install python
```

Docker should be installed:
https://www.docker.com/community-edition

### Installing

A step by step series of examples that tell you have to get a development env running

1) Install pipenv

```
$ pip install pipenv
```

2) Proceed to project folder and install all needed dependencies

```
$ pipenv install --dev
```

At this point you could work with code, just set in your ide right path to python interpreter - virtual env that was created in previous steps.


## Build container with server:

### 1. First way - via docker-compose:

    ```
    $ docker-compose up -d
    ```

### 2. Second way - via docker:

#### Build image:

    ```
    $ docker build -t car_service .
    ```

#### Run server:

    ```
    $  docker run --rm -d -p 8000:8000 --name=car_service car_service:latest pipenv run python ./car_service.py
    ```

### Run tests:

1. Go to the project folder in terminal
2. Enter:
    ```
    $ pipenv run pytest tests/
    ```

### Check report:

1. Report will presence in the terminal
2. Report could be seen via browser -> go to the folder with project -> open file **pytest_report.html**


## Requests:

#### GET /ping

`GET /ping` -> return {"message": "Car server works"} always if it runs


#### GET /car

`GET /car` -> return any available car for rent from car list
example:
{"message": "name: Ford, model: Mustang, type: Sedan, status: 1"}

`GET /car?model='model_name'` parameter model must be get from the car list (see in file rent_car_company.py) -> return car information about that model


#### DELETE /car/<model>

`DELETE /car/<model>` parameter model must be get from the car list (see in file rent_car_company.py) -> return list with all cars


#### PATCH /car/update/<model>

`PATCH /car/update/<model>?model=model_name&name=car_name&status=car_status&type=car_type` parameter model must be get from the car list (see in file rent_car_company.py) -> return car information about that model




## Authors
@grosha
