from flask import Flask, render_template_string
from suma_lista import suma_lista

app = Flask(__name__)

with open("index.html", "r", encoding="utf-8") as f:
    HTML_TEMPLATE = f.read()


@app.route("/")
def home():
    ejemplo = [1, 2, 3]
    resultado = suma_lista(ejemplo)
    return render_template_string(HTML_TEMPLATE, lista=ejemplo, resultado=resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)