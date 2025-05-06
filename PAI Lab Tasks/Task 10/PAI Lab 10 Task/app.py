from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hello! How can I assist you with university admissions?",
    "hi": "Hi there! Ask me anything about courses, deadlines, or procedures.",
    "admission process": "To apply, please visit our admissions portal and fill the form.",
    "deadline": "The last date to apply is June 15, 2025.",
    "courses": "We offer B.Tech, MBA, BSc, BBA, and many other programs.",
    "scholarship": "Yes, we provide merit-based scholarships.",
    "thank you": "You're welcome! Feel free to ask more.",
    "bye": "Goodbye! All the best for your admission."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.form["msg"].lower()
    for key in responses:
        if key in user_msg:
            return jsonify({"reply": responses[key]})
    return jsonify({"reply": "Sorry, I didn't understand that. Please ask something else."})

if __name__ == "__main__":
    app.run(debug=True)
