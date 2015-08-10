from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home",methods=['GET'])
@app.route("/",methods=['GET'])
def home():
    return render_template("index.html")
    
@app.route("/details",methods=['GET'])
def details():
    return render_template("details.html")

@app.route("/contact",methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route("/location",methods=['GET'])
def location():
    return render_template("location.html")
    
    
    
if __name__ == "__main__":
    app.debug=True
    app.run("0.0.0.0",port=80)
