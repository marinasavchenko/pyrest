from flask import Flask, jsonify

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
    pass


# GET dealer/{dealerName}
@restapp.route('/dealer/<string:name>', methods=['GET'])
def get_dealer(name):
    pass


# GET dealer/
@restapp.route('/dealer', methods=['GET'])
def get_dealers():
    return jsonify({'dealers': dealers})


# POST dealer/{dealerName}/{car}
@restapp.route('/dealer/<string:name>/car', methods=['POST'])
def create_car():
    pass


# GET dealer/{dealerName}/{car}
@restapp.route('/dealer/<string:name>/car', methods=['GET'])
def get_car():
    pass


restapp.run(port=5000)
