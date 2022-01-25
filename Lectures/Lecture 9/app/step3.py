from flask import Flask


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()


# ========================================
# Routing
# ========================================
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/boo')
def woo():
    return 'foo'


# ========================================
# Variable
# ========================================
@app.route('/name/<string:name>')  # we are using type converter here
def show_name(name):
    return f'Name {name}'


# ========================================
# Variable
# ========================================
from flask import request


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "This is a POST method"
    else:
        return "This is a GET method"


if __name__ == '__main__':
    app.run("localhost", port=5000)
