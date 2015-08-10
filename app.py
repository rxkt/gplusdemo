from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/details")
def details():
    return render_template("details.html")

@app.route("/contact")
def contact():
    return render_templates("contact.html")

@app.route("/location")
def location():
    return render_template("location.html")
    
    
    
if __name__ == "__main__":
    app.debug=True
    app.run("0.0.0.0",port=80)
