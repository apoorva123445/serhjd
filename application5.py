from flask import Flask

from flask import Flask,render_template,request
from flask_cors import cross_origin
import pickle
application5 =  Flask(__name__)

@application5.route("/",methods = ['Get'])
@cross_origin()
def homepage():
    return render_template("index.html")
@application5.route("/predict",methods = ['POST','GET'])
@cross_origin()
def index():
    if request.method == "POST" :
        try:
            gre_score = float(request.form["gre_score"])
            toefl_score = float(request.form["toefl_score"])
            university_rating = float(request.form["university_rating"])
            sop = float(request.form["sop"])
            lor = float(request.form["lor"])
            cgpa = float(request.form["cgpa"])
            is_research = request.form["research"]
            if(is_research == 'yes'):
                research = 1
            else:
                research = 0
            filename = 'finalmodel.pickle'
            loaded_model = pickle.load(open(filename,'rb'))
            prediction = loaded_model.predict([[gre_score,toefl_score,university_rating,sop,lor,cgpa,research]])
            print('prediction is', prediction)
            return render_template('result.html',prediction = round(100*prediction[0]))
        except Exception as e :
            print('the Exception message is :',e)
            return 'something is wrong'
    else:
        return render_template(index.html)


if __name__ == '__main__':
    print('app is working')
    application5.run()

