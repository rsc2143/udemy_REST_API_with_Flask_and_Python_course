from flask import Flask

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

#POST : used to receive data
#GET : used to send data

# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string_name>
@app.route('/store/<string:name>') # 'https://127.0.0.1:5000/store/some_name'     a
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    pass

# POST /store/<string_name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string_name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


app.run(port=5000)
