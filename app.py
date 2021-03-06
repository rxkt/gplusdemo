from flask import Flask, render_template, request

app = Flask(__name__)

'''
plans:
change temapltes/* to templates/en,sp,cn/*

'''

@app.route("/home",methods=['GET'])
@app.route("/",methods=['GET'])
def home():
    if len(request.args) > 0:
        if request.args["lang"]=="cn":
            print "returned cn"
            return render_template("index_cn.html")
        elif request.args["lang"]=="sp":
            print "returned sp"
            return render_template("index_sp.html")
    return render_template("index_en.html")

@app.route("/details",methods=['GET'])
def details():
    if len(request.args) > 0:
        if request.args["lang"]=="cn":
            return render_template("details_cn.html")
    return render_template("details_en.html")

@app.route("/contact",methods=['GET'])
def contact():
    if len(request.args) > 0:
        if request.args["lang"]=="cn":
            return render_template("contact_cn.html")
    return render_template("contact_en.html")

@app.route("/location",methods=['GET'])
def location():
    if len(request.args) > 0:
        if request.args["lang"]=="cn":
            return render_template("location_cn.html")
    return render_template("location_en.html")
@app.route("/media",methods=["get"])
def media():
    if len(request.args) > 0:
        if request.args["lang"]=="cn":
            return render_template("media_cn.html")
    return render_template("media_en.html")
    
    
if __name__ == "__main__":
    app.debug=True
    app.run("0.0.0.0",port=80)
