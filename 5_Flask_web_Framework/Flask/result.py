from flask import Flask,render_template

#WSGI(Web Server Gateway Interface)

app=Flask(__name__)


@app.route('/')
def main():
    return "Welcome to flask framwork class"
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")



# @app.route('/getResult/<int:score>')
# def get_result(score):
#     res=""
#     if(score>50):
#         res="Passed"
#     else:
#         res="failed"
#     return render_template('result.html',results=res)

# --------------------------------------

# pass the key value

@app.route('/getResult/<int:score>')
def get_res(score):
    res=""
    if(score<50):
        res="failed"
    else:
        res="passed"
    exp={'score':score,'result':res}
    return render_template('result.html',results=exp)
        



if __name__=="__main__":
    app.run(debug=True)