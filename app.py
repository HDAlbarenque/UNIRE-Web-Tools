import requests
from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


def comprobar_url(url):
    try:
        response = requests.get(url)
        return response
    except:
        return None


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
        msg_check = comprobar_url(url)
        if msg_check != None:
            codigo = msg_check.status_code
            mensaje = msg_check.reason
        return redirect("/verif")
    else:
        return render_template("verificar_url.html")


if __name__ == "__main__":
    app.run(debug=True)
