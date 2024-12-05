from flask import Flask,render_template
''''
it creates an instance of the Flask class
which will be your WSGI(Web Server Gateway Interface) App;icaton
'''
app = Flask(__name__) #instance of the Flask class


@app.route("/")
def home():
    return "<html><h1>welcome to my page</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html')

# render_template will redirect to the particular html page
if __name__ == "__main__":      # Entry point of any app
    app.run(debug=True)