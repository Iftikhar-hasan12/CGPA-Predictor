from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
# updated API version 4

model = pickle.load(open("model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["experience"]
    # exp-01 is going on
    prediction = model.predict([[data]]) ** 20
    return jsonify({"salary": int(prediction[0])})

app.run(debug=True)