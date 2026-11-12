import os
import pymysql
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "unfd-chave-local")

ALUNO = "Caio Gabriel Ferreira de Paula"
ATIVIDADE = "Atividade 4"


def conectar_bd():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


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
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        assunto = request.form.get("assunto", "").strip()
        descricao = request.form.get("descricao", "").strip()

        if not (nome and email and assunto and descricao):
            flash("Preencha todos os campos para enviar sua mensagem.", "erro")
            return redirect(url_for("contato"))

        conexao = conectar_bd()
        try:
            with conexao.cursor() as cursor:
                sql = """
                    INSERT INTO mensagens (nome, email, assunto, descricao)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(sql, (nome, email, assunto, descricao))
            conexao.commit()
        finally:
            conexao.close()

        flash("Mensagem enviada. Nossa equipe responde no e-mail informado.", "sucesso")
        return redirect(url_for("listar"))

    return render_template("contato.html")


@app.route("/listar")
def listar():
    conexao = conectar_bd()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, nome, email, assunto, descricao, criado_em
                FROM mensagens
                ORDER BY id DESC
                """
            )
            mensagens = cursor.fetchall()
    finally:
        conexao.close()

    return render_template("listar.html", mensagens=mensagens)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
