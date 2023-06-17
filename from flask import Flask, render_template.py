from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "YOUR_API_KEY"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=100
    )

    generated_text = response.choices[0].text.strip()
    return generated_text


if __name__ == '__main__':
    app.run(debug=True)
