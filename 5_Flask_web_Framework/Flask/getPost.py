from flask import Flask,render_template,request

#WSGI(Web Server Gateway Interface)


#jinja2 template enginee
''' 
 {{ }} => express to print output in the html
 {%   %} => express to condition for lope
 {#  #} => this is for comment
'''
app=Flask(__name__)


@app.route('/')
def main():
    return "Welcome to flask framwork class"


@app.route('/getValue',methods=['GET','POST'])
def getPost():
    # variable rule
    if request.method=='POST':
        # get the variable value from the form
        name=request.form['name']
        # redirect the form with variable
        return render_template('display.html',name=name)
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)

