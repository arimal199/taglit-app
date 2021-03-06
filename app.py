from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def base():
    return render_template('base.html')


@app.route("/login")
def auth():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
