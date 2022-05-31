from flask import Flask, request
from model import load
import pandas as pd

app = Flask(__name__)

logged_model = 'runs:/[id]'

# Load model as a PyFuncModel.
model = load(logged_model)

columns = []


@app.route("/")
def home():
    return "ok"


@app.route("/invocations", methods=["POST"])
def predict():
    data = request.get_json()
    data_input = [[data[col] for col in columns]]

    predict = model.predict(pd.DataFrame(data_input))
    result = {
        "predict": predict[0]
    }
    return result


app.run(host="0.0.0.0", port=8080)
