from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
openai.api_key = "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"

app = Flask(__name__)
CORS(app)


# basic API implementation

"""
@app.route('/process-user-input', methods=['POST'])
def process_user_input():
    data = request.get_json()
    user_input = data['input']

    # Process the user input as needed
    # For demonstration purposes, we will simply return the input as the output
    output = user_input

    return jsonify({'message': output})


if __name__ == '__main__':
    app.run(debug=True)

"""


@app.route('/api/chatbot', methods=['POST'])
def chatbot():
    user_prompt = request.json['prompt']

    response = openai.ChatCompletion.create(
        engine='davinci',
        prompt=user_prompt,
        max_tokens=100,
        temperature=0.8,
        n=1,
        stop=None
    )
    output = format_response(response)

    # generated_response = response.choices[0].text.strip()
    return jsonify({'message': output})


if __name__ == '__main__':
    app.run(debug=True)


def process_api_response(api_response):
    destinations = []

    for choice in api_response.choices:
        destination = {}

        # Extract destination name
        destination['name'] = extract_destination_name(choice.text)

        # Extract destination description
        destination['description'] = extract_destination_description(
            choice.text)

        # Extract destination imagery
        # destination['imagery'] = extract_destination_imagery(choice.text)

        # Add the destination to the list
        destinations.append(destination)

    return destinations


def extract_destination_name(text):
    # Split the text into lines to find the line containing the destination name
    lines = text.split('\n')

    # Iterate over the lines and extract the destination name
    for line in lines:
        # Perform any necessary text processing or pattern matching to extract the name
        if 'Destination Name:' in line:
            extracted_name = line.split(':')[1].strip()
            return extracted_name

    # Return a default name if the destination name is not found
    return 'Unknown Destination'


def extract_destination_description(text):
    # Split the text into lines to find the line containing the destination description
    lines = text.split('\n')

    # Iterate over the lines and extract the destination description
    for line in lines:
        # Perform any necessary text processing or pattern matching to extract the description
        if 'Description:' in line:
            extracted_description = line.split(':')[1].strip()
            return extracted_description

    # Return a default description if the destination description is not found
    return 'No description available.'


def extract_destination_imagery(text):
    # Split the text into lines to find the line containing the destination imagery
    lines = text.split('\n')

    # Iterate over the lines and extract the destination imagery
    for line in lines:
        # Perform any necessary text processing or pattern matching to extract the imagery
        if 'Imagery:' in line:
            extracted_imagery = line.split(':')[1].strip()
            return extracted_imagery

    # Return a default imagery if the destination imagery is not found
    return 'No imagery available.'


def format_response(api_response):
    destinations = process_api_response(api_response)

    formatted_destinations = []
    for destination in destinations:
        formatted_destination = {
            'name': destination['name'],
            'description': destination['description'],
            'imagery': destination['imagery']
        }
        formatted_destinations.append(formatted_destination)

    return {'destinations': formatted_destinations}
