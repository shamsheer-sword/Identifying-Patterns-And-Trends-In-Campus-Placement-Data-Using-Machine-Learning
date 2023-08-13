from flask import Flask, render_template,request
import pickle
import joblib
app=Flask(__name__)
model=pickle.load(open("placement.pkl",'rb'))
ct=joblib.load('placement.pkl')
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/guest',methods=["POST"])
def Guest():
    sen1=request.form["sen1"]
    sen2=request.form["sen2"]
    sen3=request.form["sen3"]
    sen4=request.form["sen4"]
    sen5=request.form["sen5"]
    sen6=request.form["sen6"]
    sen7=request.form["sen7"]

@app.route('/y_predict',methods=["POST"])
def y_predict():
    x_test = [
        int(request.form["sen2"]),
        int(request.form["sen1"]),
        int(request.form["sen3"]),
        int(request.form["sen4"]),
        int(request.form["sen5"]),
        int(request.form["sen6"]),
        int(request.form["sen7"])
    ]
    x_test=[x_test]
    prediction = model.predict(x_test)
    prediction=prediction[0]
    return render_template("secondpage.html",y=prediction)
app.run(debug=True)