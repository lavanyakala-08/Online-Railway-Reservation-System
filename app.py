from flask import Flask, request, jsonify
from database import initialize_database
import user
import booking

app = Flask(__name__)

# Initialize DB when the app starts
initialize_database()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    res = user.register_user(data.get('username'), data.get('password'), data.get('email'))
    return jsonify(res)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    res = user.login_user(data.get('username'), data.get('password'))
    return jsonify(res)

@app.route('/trains', methods=['GET'])
def get_trains():
    return jsonify(booking.view_trains())

@app.route('/book', methods=['POST'])
def book():
    data = request.json
    res = booking.book_ticket(data.get('user_id'), data.get('train_id'), data.get('seats_booked'))
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
