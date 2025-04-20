## Building url Dynamically
# variable Rule
## jinja2  Template Engine

### jinja2  Template Engine

'''
Jinja2 is a template engine for Python. It is a library that allows you to create dynamic web pages using a simple and easy-to-use syntax.
{{  }} - expressions to print output in html
{%  %} - control structures,for looping,if else statements
{#  #} - comments
'''

from flask import Flask,render_template,request,redirect,url_for
''''
it creates an instance of the Flask class
which will be your WSGI(Web Server Gateway Interface) App;icaton
'''
app = Flask(__name__) #instance of the Flask class

@app.route("/")
def home():
    return "<html><h1>welcome to my page</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')

#Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res="" 
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template('result.html',result=res)

#Variable Rule
@app.route('/successres/<int:score>')
def successres(score):
    res="" 
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    exp = {'score':score,'result':res}
    return render_template('result1.html',result=exp)

#if Condition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('results2.html',results=score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        english=float(request.form['English'])
        maths=float(request.form['maths'])
        social=float(request.form['social'])
        total_score=(science+english+maths+social)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=total_score))
# render_template will redirect to the particular html page
if __name__ == "__main__":      # Entry point of any app
    app.run(debug=True)

