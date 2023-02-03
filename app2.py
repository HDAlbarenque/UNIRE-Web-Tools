from flask import Flask, render_template, redirect, request
#

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


def comprobar_url(url):
    url = request.args.get("url")
    try:
        return request.get(url)
    except request.exceptions.RequestException as e:
        return -1


def comprobar_msg(return_code):
    if return_code <= 400:
        if return_code < 0:
            return "Problemas de red"
        else:
            return "La web no está funcionando"
    else:
        return "Web OK"


@app.route("/verif", methods=["GET", "POST"])
def verificar_url():
    if request.method == "POST":
        url = request.form.get("ht_url")
        msg_check = comprobar_msg(comprobar_url(url))
        return redirect("/verif")
    else:
        return render_template("verificar_url.html")


if __name__ == "__main__":
    app.run(debug=True)
