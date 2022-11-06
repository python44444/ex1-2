from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def api():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def api2():
    answer = request.form["animal"]
    if answer == "cat":
        return "cat"
    elif answer == "dog":
        return "dog"
    else:
        return "fox"
    return render_template("post.html", answer=answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)
