from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name': 'My item',
            'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return(render_template('index.html'))
#POST : used to receive data
#GET : used to send data

# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)

    return(jsonify(new_store))

# GET /store/<string_name>
@app.route('/store/<string:name>') # 'https://127.0.0.1:5000/store/some_name'     a
def get_store(name):
    # Iterate over store
    # if the store name matches, return it
    # if the store name does not match, return an error message
    for store in stores:
        if(name == store['name']):
            return(jsonify(store))
    return(jsonify({'message': 'store not found'}))

# GET /store
@app.route('/store')
def get_stores():
    return(jsonify({'stores': stores}))

# POST /store/<string_name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if(name == store['name']):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return(jsonify(store))
    return(jsonify({'message': 'store not found'}))

# GET /store/<string_name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if(name == store['name']):
            return(jsonify({'items': store['items']}))
        else:
            return(jsonify({'message': 'store not found'}))


app.run(port=5000)
