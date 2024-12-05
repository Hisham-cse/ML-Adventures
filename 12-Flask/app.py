from flask import Flask
''''
it creates an instance of the Flask class
which will be your WSGI(Web Server Gateway Interface) App;icaton
'''
app = Flask(__name__) #instance of the Flask class


@app.route("/")
def home():
    return "Welcome to Home Page"

@app.route("/contact")
def Contact():
    return "This is my Contact Page"

if __name__ == "__main__":      # Entry point of any app
    app.run(debug=True)