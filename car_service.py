from flask import Flask, jsonify, request

from rent_car_company import list_cars, Car, get_value_list_cars

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Car server works'})


@app.route('/car', methods=['GET', 'POST'])
def car():
    if request.method == 'GET':
        counter = 0
        for car in list_cars:
            if request.form['model'] == car.get_model():
                return jsonify({'message': car.get_car_info()})
            else:
                counter += 1
                if car.get_status() == 1:
                    try:
                        return jsonify({'message': car.get_car_info()})
                    finally:
                        car.status = 0
                if counter is len(list_cars):
                    return jsonify({'message': 'No free car available'})
    elif request.method == 'POST':
        # '{"name":"value1", "model":"value2", "type":"value2", "status":1}'
        response = request.json
        list_cars.add(Car(name=response['name'], model=response['model'],
                          type=response['type'], status=response['status']))
        return jsonify({'message': get_value_list_cars()})


@app.route('/car/<model>', methods=['DELETE'])
@app.route('/car/<model>/update', methods=['PATCH'])
def car(model=None):
    if request.method == 'DELETE':
        counter = 0
        for car in list_cars:
            counter += 1
            if car.get_model() == model:
                list_cars.remove(car)
                return jsonify({'message': get_value_list_cars()})
            if counter is len(list_cars):
                return jsonify({'message': 'That car is absent in the list'})
    elif request.method == 'PATCH':
        counter = 0
        for car in list_cars:
            counter += 1
            if car.get_model() == model:
                if request.form['status']:
                    car.status == request.form['status']
                if request.form['model']:
                    car.status == request.form['model']
                if request.form['type']:
                    car.status == request.form['type']
                if request.form['name']:
                    car.status == request.form['name']
                return jsonify({'message': car.get_car_info()})
            if counter is len(list_cars):
                return jsonify({'message': 'That car is absent in the list'})


@app.route('/car_list', methods=['GET'])
def car_list():
    return jsonify({'message': get_value_list_cars()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
