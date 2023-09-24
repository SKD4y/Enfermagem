from flask import Flask, render_template, request, make_response, Response
from init_db import database_class

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        nome = request.form.get('nome')  # Pega os dados do formulario com name = 'nome'
        idade = request.form.get('idade')  # Pega os dados do formulario com name = 'idade'
        sexo = request.form.get('sexo')  # Pega os dados do formulario com name = 'sexo'
        con = database_class()
        con.inserir_no_banco(nome=nome, idade=idade, sexo=sexo)

    return render_template("index.html")


@app.route("/database")
def database():

    db = database_class()  # Chama a classe da database
    data_json = db.retornar_dados()  # Retorna os dados da database em JSON
    db.commit_fechar_banco()  # Fecha a conexão com o banco

    # Deixar a visualização mais bonita e legível
    response = Response(data_json, content_type='application/json; charset=utf-8')
    response.headers['Content-Disposition'] = 'inline; filename=data.json'
    return response


@app.route("/deleteData")
def delete():
    db = database_class()
    statement = db.deletar_dados()

    if statement:
        # Se a operação foi bem-sucedida, retorne uma resposta HTTP 200 OK
        response = make_response("Data deleted successfully", 200)
    else:
        # Se a operação falhou, retorne uma resposta HTTP 500 Internal Server Error
        response = make_response("Error deleting data", 500)
    
    return response


if __name__ == "__main__":
    app.run(debug=True)
