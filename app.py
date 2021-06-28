from flask import Flask,render_template,request

import joblib

app=Flask(__name__)

model=joblib.load("weight_model.pkl")

@app.route('/')
def hello():
	return render_template("index.html")

@app.route('/',	 methods= ['POST'])
def submit():
	if request.method == 'POST':
		height = float(request.form['height'])

		weight=str(model.predict([[height]]) [0])

	return render_template("index.html", your_weight= weight)



if __name__ == '__main__':
	app.run(debug=True)