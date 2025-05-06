from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('email_classifier.pkl')


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        email = request.form['email']
        prediction = model.predict([email])[0]
        result = f"Category: {prediction}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
