# Example of Register

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for registered users (replace with a database in a production environment)
users = []

@app.route('/api/register', methods=['POST'])
def register():
    # Retrieve user data from the request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    # Validate the user data
    if not username or not password or not email:
        return jsonify({'error': 'Please provide a username, password, and email.'}), 400

    # Check if the username or email is already taken
    if any(user['username'] == username for user in users):
        return jsonify({'error': 'Username is already taken.'}), 409
    if any(user['email'] == email for user in users):
        return jsonify({'error': 'Email is already taken.'}), 409

    # Create a new user
    user = {'username': username, 'password': password, 'email': email}
    users.append(user)

    return jsonify({'message': 'User registered successfully.'}), 201

if __name__ == '__main__':
    app.run(debug=True)
