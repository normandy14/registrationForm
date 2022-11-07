from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def html_form():
     return render_template("app.html")

if __name__ == "__main__":
   app.run()