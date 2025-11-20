from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("dtmodel.pkl", "rb"))


sex_map = {"F": 0, "M": 1}
bp_map = {"HIGH": 2, "LOW": 1, "NORMAL": 0}
chol_map = {"HIGH": 1, "LOW": 0}

drug_map_reverse = {
    0: "drugA",
    1: "drugB",
    2: "drugC",
    3: "drugX",
    4: "drugY"
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    sex = sex_map[request.form['sex']]
    bp = bp_map[request.form['bp']]
    chol = chol_map[request.form['chol']]
    na_k = float(request.form['na_k'])

    features = np.array([[age, sex, bp, chol, na_k]])
    pred = model.predict(features)[0]

    drug = drug_map_reverse[pred]

    return render_template("index.html", prediction_text=f"Predicted Drug: {drug}")

if __name__ == "__main__":
    app.run(debug=True)
