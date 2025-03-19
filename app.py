from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the trained model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        data = vectorizer.transform([message])  # Convert input to numerical form
        prediction = model.predict(data)[0]  # Predict spam or ham
        result = "Spam" if prediction == 1 else "Not Spam"
        return render_template('index.html', prediction_text=f'Result: {result}')

if __name__ == '__main__':
    app.run(debug=True)
