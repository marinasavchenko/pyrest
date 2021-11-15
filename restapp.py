from flask import Flask, jsonify, request

restapp = Flask(__name__)

dealers = [
    {
        'name': 'Dealer1',
        'cars': [
            {
                'name': 'BMW',
                'price': 30000
            }
        ]
    }
]


# POST dealer/{dealerName}
@restapp.route('/dealer', methods=['POST'])
def create_dealer():
    request_data = request.get_json()
    dealer = {
        'name': request_data['name'],
        'cars': []
    }
    dealers.append(dealer)
    return jsonify(dealer)


# GET dealer/{dealerName}
@restapp.route('/dealer/<string:name>', methods=['GET'])
def get_dealer(name):
    for dealer in dealers:
        if dealer['name'] == name:
            return jsonify(dealer)
        return jsonify({'message': 'dealer is not found'})


# GET dealer/
@restapp.route('/dealer', methods=['GET'])
def get_dealers():
    return jsonify({'dealers': dealers})


# POST dealer/{dealerName}/{car}
@restapp.route('/dealer/<string:name>/car', methods=['POST'])
def create_car(name):
    request_data = request.get_json()
    for dealer in dealers:
        if dealer['name'] == name:
            car = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            dealer['cars'].append(car)
            return jsonify(car)
        return jsonify({'message': 'dealer is not found'})


# GET dealer/{dealerName}/{car}
@restapp.route('/dealer/<string:name>/car', methods=['GET'])
def get_car(name):
    for dealer in dealers:
        if dealer['name'] == name:
            return jsonify({'cars': dealer['cars']})
        return jsonify({'message': 'cars are not found'})


restapp.run(port=5000)
