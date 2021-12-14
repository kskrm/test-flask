from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    team = ["Real Madrid","Manchester United","FC Barcelona","Manchester City"]
    return render_template("index.html",name=name, team=team)

@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    team = ["Real Madrid","Manchester United","FC Barcelona","Manchester City"]
    return render_template("index.html", name=name, team=team)

if __name__ == "__main__":
    app.run(debug=True)