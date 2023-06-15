import pickle

from flask import Flask, render_template, request


app = Flask(__name__)
file = open('model.pkl', 'rb')
regr = pickle.load(file)
file.close()


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/car_sales_analysis")
def car_sales_analysis():
    return render_template('car_sales_analysis.html')


@app.route("/emission_analysis")
def emission_analysis():
    return render_template('emission_analysis.html')


@app.route("/predict_car_price")
def predict_car_price():
    return render_template('predict_car_price.html')


@app.route("/predict_emission", methods=["GET", "POST"])
def predict_emission():
    if request.method == "POST":
        myDict = request.form
        engine = float(myDict['engine'])
        input_size = [engine]
        value = regr.predict([input_size])[0][0]

        return render_template('predict_emission.html', EMI=round(value))

    return render_template('predict_emission.html', EMI=0.00)


if __name__ == '__main__':
    app.run(debug=True)
