from flask import Flask, render_template_string
from suma_lista import suma_lista

app = Flask(__name__)

with open("index.html", "r", encoding="utf-8") as archivo:
    plantilla = archivo.read()


@app.route("/")
def inicio():
    lista = [1, 2, 3]
    resultado = suma_lista(lista)
    return render_template_string(plantilla, lista=lista, resultado=resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)