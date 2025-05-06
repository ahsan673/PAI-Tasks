from flask import Flask, render_template, request
from textblob import TextBlob
from transformers import pipeline, set_seed
import difflib

app = Flask(__name__)

# Load a transformer pipeline for sentence completion (GPT-2)
text_generator = pipeline("text-generation", model="gpt2")
set_seed(42)


def get_corrections(original_text):
    blob = TextBlob(original_text)
    corrected_text = str(blob.correct())

    # Count differences
    diff = list(difflib.ndiff(original_text.split(), corrected_text.split()))
    changes = [word for word in diff if word.startswith('- ') or word.startswith('+ ')]
    num_corrections = len([c for c in changes if c.startswith('- ')])

    return corrected_text, num_corrections, changes


def complete_sentence(text):
    # Ensure the input is not too long
    prompt = text.strip()
    if not prompt.endswith(('.', '?', '!')):
        prompt += '.'
    
    generated = text_generator(prompt, max_length=50, num_return_sequences=1)
    completed_text = generated[0]['generated_text']

    return completed_text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_text']
    corrected_text, num_corrections, changes = get_corrections(user_input)
    completed_text = complete_sentence(corrected_text)

    return render_template(
        'result.html',
        original=user_input,
        corrected=corrected_text,
        completed=completed_text,
        num_corrections=num_corrections,
        changes=changes
    )


if __name__ == '__main__':
    app.run(debug=True)
