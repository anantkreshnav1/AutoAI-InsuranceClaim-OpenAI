import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = “<OPEN AI KEY>”  // provide the generated open ai key here

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    accident_report = request.form['accident_report']

    # Send the accident report to GPT-3 for decision
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Based on the following accident report, should the insurance claim be approved or denied as Decision? Provide the reason for approval or denial as Reason\n\n{accident_report}\n\nDecision:",
        max_tokens=1000
    )

    decision = response.choices[0].text.strip()

    return render_template('result.html', decision=decision)

if __name__ == '__main__':
        app.run(debug=True, host="0.0.0.0")
