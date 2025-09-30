from flask import Flask,request,render_template,redirect,url_for

app=Flask(__name__)


@app.route('/getResult/<int:score>')
def getResult(score):
    res=""
    if(score<50):
        res="failed"
    else:
        res="passed"
    exp={'score':score,'result':res}
    return render_template('result.html',results=exp)
        

@app.route('/submit_marks',methods=['GET','POST'])
def submit_marks():
    total_marks=0
    if request.method=='POST':
        math = float(request.form['math'])
        English = float(request.form['english'])
        physics = float(request.form['physics'])
        ict = float(request.form['ict'])
        total_marks = (math + English + physics + ict) / 4
    else:
        return render_template('marks.html')
    return redirect(url_for('getResult',score=total_marks))
    
    


if __name__=="__main__":
    app.run(debug=True)