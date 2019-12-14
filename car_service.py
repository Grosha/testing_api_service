import json

from flask import Flask, jsonify, request

from rent_car_company import list_cars, Car, get_value_list_cars

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Car server works'})


@app.route('/car', methods=['GET', 'POST'])
def car():
    if request.method == 'GET':

        args = request.args
        if len(args) > 0:
            counter = 0
            if 'model' in args:
                model = args.get('model', type=str)
                if model:
                    for car in list_cars:
                        counter += 1
                        if model.lower() == car.get_model().lower():
                            return jsonify({'message': car.get_car_info()})
                        if counter == len(list_cars):
                            return jsonify({'message': f'Car model {model} is absent in the list'})
                else:
                    return jsonify({'message': f'Car model {model} is not written'})
            else:
                return jsonify({'message': 'Incorrect parameter'})
        else:
            counter = 0
            for car in list_cars:
                counter += 1
                if car.get_status() == 1:
                    try:
                        return jsonify({'message': car.get_car_info()})
                    finally:
                        car.status = 0
                if counter is len(list_cars):
                    return jsonify({'message': 'No free car available'})
    elif request.method == 'POST':
        # new_car = request.json
        try:
            new_car = json.loads(request.json)
            if new_car['model']:
                for car in list_cars:
                    model = new_car['model']
                    if model.lower() == car.get_model().lower():
                        return jsonify({'message': f'Car presence in the list: {car.get_car_info()}'})
                list_cars.add(Car(name=new_car['name'], model=new_car['model'],
                                  type=new_car['type'], status=new_car['status']))
                # return jsonify({'message': get_value_list_cars()})
                return jsonify({'message': 'New car added'})
            else:
                return jsonify({'message': f'Incorrect json body for object Car: {new_car}'})
        except KeyError as e:
            print(e)
            return jsonify({'message': f'Incorrect parameter {e} in json body for object Car'})
        except Exception as e:
            print(e)
            return jsonify({'message': f'Problem with json {e}'})


@app.route('/car/<model>', methods=['DELETE'])
def delete_car(model):
    if request.method == 'DELETE':
        if model:
            counter = 0
            for car in list_cars:
                counter += 1
                if car.get_model().lower() == model.lower():
                    list_cars.remove(car)
                    # return jsonify({'message': get_value_list_cars()})
                    return jsonify({'message': f'Car model {model} removed'})
                if counter is len(list_cars):
                    return jsonify({'message': 'That car is absent in the list'})


@app.route('/car/update/<model>', methods=['PATCH'])
def update_car(model):
    if request.method == 'PATCH':
        if model:
            counter = 0
            for car in list_cars:
                counter += 1
                if car.get_model().lower() == model.lower():
                    if request.args.get('status', type=str):
                        car.status = request.args.get('status')
                    elif request.args.get('model', type=str):
                        car.model = request.args.get('model')
                    elif request.args.get('type', type=str):
                        car.type = request.args.get('type')
                    elif request.args.get('name', type=str):
                        car.name = request.args.get('name')
                    return jsonify({'message': car.get_car_info()})
                if counter is len(list_cars):
                    return jsonify({'message': 'That car is absent in the list'})
            else:
                return jsonify({'message': "Model name wasn't added"})


@app.route('/car_list', methods=['GET'])
def car_list():
    return jsonify({'message': get_value_list_cars()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
