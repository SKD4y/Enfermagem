import sqlite3
import json


class database_class():
    def __init__(self) -> None:
        """Quando um objeto é criado, """

        # Inicia a conexão com o banco
        self.con = sqlite3.connect('database.db')

        # Permite o acesso dos dados pelo nome da coluna
        self.con.row_factory = sqlite3.Row

        # "um objeto que permite que você execute comandos SQL no banco de dados e interaja com os resultados dessas consultas."
        self.cur = self.con.cursor()

        self.create_usuarios()

    def create_usuarios(self):
        """Executa o script SQL dentro do arquivo "schema.sql". O arquivo database.db criado representa o banco de dados"""
        # Cria a tabela usuários
        with open('schema.sql') as f:
            self.con.executescript(f.read())

    def commit_fechar_banco(self) -> None:
        """Fecha a conexão com o banco e salva alterações"""
        self.con.commit()
        self.con.close()

    def inserir_no_banco(self, nome, idade, sexo):
        """Insere dados no banco e salva as alterações"""
        self.cur.execute("INSERT INTO usuarios (nome, idade, sexo) VALUES (?, ?, ?)",
                         (nome, idade, sexo))
        self.commit_fechar_banco()

    def deletar_dados(self):
        """Deleta TODOS os dados da tabela usuário"""
        try:
            self.cur.execute("DELETE FROM usuarios")
            self.commit_fechar_banco()
            return True
        except sqlite3.Error as error:
            return error

    def retornar_dados(self):
        """Retorna os dados da tabela usuarios"""
        self.cur.execute("SELECT * FROM usuarios")
        data = self.cur.fetchall()

        data_dict_list = []
        for row in data:  # Looping que retorna todos os dados da tabela usuários e os coloca em "data_dict_list"
            data_dict = {
                'nome': row['nome'],
                'idade': row['idade'],
                'sexo': row['sexo']
            }
            data_dict_list.append(data_dict)

        # Formata a lista para o formato JSON (Javascript Object Notation)
        data_json = json.dumps(data_dict_list, indent=4)
        return data_json  # retorna os dados Json


# Se o arquivo que você executar for esse, ao invés do "site_enfermagem.py", ele vai executar o código abaixo
if __name__ == "__main__":
    db = database_class()
    data_json = db.retornar_dados()
    db.commit_fechar_banco()

    print(data_json)  # Printa os dados da tabela usuário
