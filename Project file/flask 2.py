from Flask import flask, render_template, request


literacy = flask(__name__) # initializng the flask app


@literacy.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
       literacy.run(debug = False, port = 5000)