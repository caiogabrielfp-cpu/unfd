from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os
from dotenv import load_dotenv

FRONTEND_DIR = Path(__file__).resolve().parents[2] / "frontend"

app = Flask(__name__)

ALUNO = "Caio gabriel Ferreira de Paula"
ATIVIDADE = "Atividade 3 - Deploy Flask na AWS EC2"

def conectar_bd():
 conexao = pymysql.connect(
 host="18.234.53.187",
 user="caio",
 password="caio",
 database="escola",
 cursorclass=pymysql.cursors.DictCursor
 )
 return conexao
        
@app.context_processor
def dados_do_rodape():
    return {"aluno": ALUNO, "atividade": ATIVIDADE}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contato", methods=["GET", "POST"])
def contato():
    if request.method == "POST":
        nome = request.form.get("nome")
        curso = request.form.get("curso")
        

        conexao = conectar_bd()
        with conexao.cursor() as cursor:
            sql = "INSERT INTO alunos (nome, curso) VALUES (%s, %s)"
            cursor.execute(sql, (nome, curso))
            conexao.commit()
            conexao.close()
            return redirect(url_for("listar_alunos"))
            return render_template("novo_aluno.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
