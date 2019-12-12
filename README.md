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


## Build container with client and server:

```
$ docker build -t car_service .
```

### Run server:
run in server mode on 9666 port:

```
$  docker run --rm -d -p 8000:8000 --name=car_service car_service:latest pipenv run python ./car_service.py
$  docker run -d -p 8000:8000 --name=car_service car_service:latest pipenv run python ./car_service.py
```

### Run tests:
run in client mode :

```
$  docker run --rm --name=gitlab_api_stub_client gitlab_stub:latest pipenv run python ./stub_service/client_worker.py $PIPELINE_ID
```

## Requests:

#### GET /ping

`GET /ping` -> return {"message": "Car server works"} always if it runs


#### GET /car

`GET /car` -> return any available car for rent from car list
example:
{"message": "name: Ford, model: Mustang, type: Sedan, status: 1"}

`GET /car?model='model_name'` parameter model must be get from the car list (see in file rent_car_company.py) -> return car information about that model


#### POST /car

`POST /car` -> return list with all cars
example of json - '{"name":"Tesla", "model":"Model3", "type":"Sedan", "status":1}'


#### DELETE /car/<model>

`DELETE /car/<model>` parameter model must be get from the car list (see in file rent_car_company.py) -> return list with all cars


#### PATCH /car/update/<model>

`PATCH /car/update/<model>?model=model_name&name=car_name&status=car_status&type=car_type` parameter model must be get from the car list (see in file rent_car_company.py) -> return car information about that model




##
## Authors
@grosha


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc