from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/process-user-input', methods=['POST'])
def process_user_input():
    data = request.get_json()
    user_input = data['userInput']

    # Process the user input as needed
    # For demonstration purposes, we will simply return the input as the output
    output = user_input

    return jsonify({'message': output})


if __name__ == '__main__':
    app.run(debug=True)
