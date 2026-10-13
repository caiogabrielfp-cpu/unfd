from pathlib import Path

from flask import Flask, render_template

FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"

app = Flask(__name__)

ALUNO = "Caio gabriel Ferreira de Paula"
ATIVIDADE = "Atividade 3 - Deploy Flask na AWS EC2"


@app.context_processor
def dados_do_rodape():
    return {"aluno": ALUNO, "atividade": ATIVIDADE}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
